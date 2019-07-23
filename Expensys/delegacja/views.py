from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from .forms import BusinessTripForm, PlannedExpenseForm, RealizedExpenseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.db.models import Q
from .models import BusinessTrip, PlannedExpense, RealizedExpense
from pierdoly.models import Country, Employee
from django.contrib.auth.models import User

@login_required
def BusinessTripPrepare(request, delegacja_id):

    delegacja = get_object_or_404(BusinessTrip, pk=delegacja_id)

    if request.method == "POST":
        # nie wiem czy dobrze to robię ale działa, jak jedna forma jest robiona to druga nie i dlatego jest exception
        try:
            # juhu :) request.FILES - to była odpowiedź
            formPost = RealizedExpenseForm(request.POST, request.FILES)
            instance = formPost.save(commit=False)
            # musimy dodawać delegacje bo jest usunięta z widocznych pól w formie
            instance.delegacja = delegacja
            instance.save()
        except:
            pass

        try:
            formPost = PlannedExpenseForm(request.POST, request.FILES)
            instance = formPost.save(commit=False)
            # musimy dodawać delegacje bo jest usunięta z widocznych pól w formie
            instance.delegacja = delegacja
            instance.save()
        except:
            pass



    # delegacja = BusinessTrip.objects.get(id=delegacja_id)
    # planowane_wydatki = PlannedExpense.objects.filter(delegacja=delegacja)
    planowane_wydatki = PlannedExpense.objects.filter(delegacja__pk=delegacja_id)
    zrealizowane_wydatki = RealizedExpense.objects.filter(delegacja__pk=delegacja_id)

    # czy kierownik
    if request.user.groups.filter(name="Kierownicy").count()>0:
        czy_kierownik = "TAK"
    else:
        czy_kierownik = "NIE"

    # czy księgowość
    if request.user.groups.filter(name="Ksiegowosc").count()>0:
        czy_ksiegowosc = "TAK"
    else:
        czy_ksiegowosc = "NIE"

    # czy pracownik który robi delegację
    if request.user.username == delegacja.pracownik.username:
        czy_delegowany = "TAK"
    else:
        czy_delegowany = "NIE"

    context = {
        'req':request,
        'delegacja': delegacja,
        #defaultowa delegacja w formie
        'formPlanned': PlannedExpenseForm(initial={'delegacja': delegacja}),
        'formRealized': RealizedExpenseForm(initial={'delegacja': delegacja}),
        'planowane_wydatki': planowane_wydatki,
        'zrealizowane_wydatki': zrealizowane_wydatki,
        'czy_kierownik': czy_kierownik,
        'czy_ksiegowosc': czy_ksiegowosc,
        'czy_delegowany': czy_delegowany,
    }
    return render(request, 'wypelnianie_delegacji.html', context)


# widok manadżera z delegacjami pracownikó do zaakceptowania
@login_required
def BusinessTripsAndExpensesToAccept(request):
    # czy kierownik
    if request.user.groups.filter(name="Kierownicy").count() > 0:
        czy_kierownik = "TAK"
    else:
        czy_kierownik = "NIE"

    me = Employee.objects.get(pracownik__username=request.user.username)
    moi_pracownicy = Employee.objects.filter(manager=me)
    moi_pracownicy1 = []
    for pracownik in moi_pracownicy:
        moi_pracownicy1.append(pracownik.pracownik)

    delegacje_do_zatwierdzenia = BusinessTrip.objects.filter(pracownik__in=moi_pracownicy1).filter(Q(akceptacja_planowanej=False) | Q(akceptacja_zrealizowanej=False)).filter(do_managera=True)
    context = {
        'delegacje_do_zatwierdzenia': delegacje_do_zatwierdzenia,
        'czy_kierownik': czy_kierownik,
        'moi_pracownicy': moi_pracownicy,
        'moi_pracownicy1': moi_pracownicy1,
        'me': me,
        'user': request.user,
    }
    return render(request, 'zatwierdzanie_delegacji.html', context)

# widok księgowości z delegacjami do zaksięgowania
@login_required
def BusinessTripsAndExpensesToBook(request):
    # czy kierownik
    if request.user.groups.filter(name="Ksiegowosc").count() > 0:
        delegacje_do_zaksiegowania = BusinessTrip.objects.filter(Q(akceptacja_zrealizowanej=True) & Q(delegacja_zaksiegowana=False))
        context = {
            'delegacje_do_zaksiegowania': delegacje_do_zaksiegowania,
        }
        return render(request, 'zaksiegowanie_delegacji.html', context)

# widok księgowości z zaakceptowanymi delegacjami
@login_required
def BusinessTripsAndExpensesBooked(request):
    # czy kierownik
    if request.user.groups.filter(name="Ksiegowosc").count() > 0:
        delegacje_zaksiegowane = BusinessTrip.objects.filter(delegacja_zaksiegowana=True)
        context = {
            'delegacje_zaksiegowane': delegacje_zaksiegowane,
        }
        return render(request, 'zaksiegowane_delegacje.html', context)



@login_required
def BusinessTripCreate(request):

    if request.method == 'POST':
        pracownik = request.user
        # znajdziemy kraj po id, ha ha
        kraj = Country.objects.get(pk=request.POST['kraj'])
        miasto = request.POST['miasto']
        #data_wniosku = request.POST['data_wniosku']
        poczatek = request.POST['poczatek']
        koniec = request.POST['koniec']

        trip = BusinessTrip.objects.create(
            pracownik=pracownik,
            kraj=kraj,
            miasto=miasto,
            #data_wniosku=data_wniosku,
            poczatek=poczatek,
            koniec=koniec,
        )
        trip.save()
        id = trip.pk
        return redirect('wypelnij_delegacje', delegacja_id=id)
    else:
        context = {
            'form':BusinessTripForm(),
        }
        return render(request, 'nowa_delegacja.html', context)

@login_required()
def BusinessTripHome(request):
    current_user = request.user
    if current_user.is_authenticated:
        delegacje_obecne = BusinessTrip.objects.filter(pracownik=current_user).filter(akceptacja_zrealizowanej=False)

        context = {
            'delegacje_obecne':delegacje_obecne,
            }
        return render(request, 'moje_delegacje.html', context)
    else:
        return redirect('home')

@login_required()
def BusinessTripDone(request):
    current_user = request.user
    if current_user.is_authenticated:
        delegacje_ukonczone = BusinessTrip.objects.filter(pracownik=current_user).filter(akceptacja_zrealizowanej=True)

        context = {
            'delegacje_ukonczone': delegacje_ukonczone,
            }
        return render(request, 'ukonczone_delegacje.html', context)
    else:
        return redirect('home')


@login_required
def BookBusinessTrip(request, delegacja_id):
    delegacja = get_object_or_404(BusinessTrip, pk=delegacja_id)
    # przechowaj __str__ delegacji i wyślij potem do messages
    if delegacja:
        # czy wszystkie wydatki zostały zaksięgowane
        zrealizowane_wydatki = RealizedExpense.objects.filter(delegacja=delegacja)
        wszystkie_wydatki_zaksiegowane=True
        for wydatek in zrealizowane_wydatki:
            if not wydatek.wydatek_zaksiegowany:
                wszystkie_wydatki_zaksiegowane = False
        if wszystkie_wydatki_zaksiegowane:
            delegacja.delegacja_zaksiegowana = True
            delegacja.save()
            messages.success(request, "Delegacji " + str(delegacja.id) + " została zaksięgowana")
            return redirect('delegacje_do_zaksiegowania')
        else:
            messages.error(request, "Nie wszystkie wydatki dla delegacji " + str(delegacja.id) + " zostały zaksięgowane.")
            return redirect('wypelnij_delegacje', delegacja_id=delegacja_id)
@login_required
def BookExpense(request, delegacja_id, wydatek_id):
    wydatek = get_object_or_404(RealizedExpense, pk=wydatek_id)
    # przechowaj __str__ delegacji i wyślij potem do messages
    if wydatek:
        wydatek.wydatek_zaksiegowany = True
        wydatek.save()
        return redirect('wypelnij_delegacje', delegacja_id=delegacja_id)

@login_required
def DeletePayment(request, delegacja_id, payment_id):
    payment = get_object_or_404(PlannedExpense, pk=payment_id)
    if payment:
        payment.delete()
    return redirect('wypelnij_delegacje', delegacja_id=delegacja_id)

@login_required
def DeleteRealizedPayment(request, delegacja_id, realized_payment_id):
    payment = get_object_or_404(RealizedExpense, pk=realized_payment_id)
    if payment:
        payment.delete()
    return redirect('wypelnij_delegacje', delegacja_id=delegacja_id)

@login_required
def DeleteBusinessTrip(request, delegacja_id):
    delegacja = get_object_or_404(BusinessTrip, pk=delegacja_id)
    # przechowaj __str__ delegacji i wyślij potem do messages
    if delegacja:
        delegacja.delete()
        messages.success(request, "Delegacja " + str(delegacja_id) + " zostały usunięta")
    return redirect('business_trip_home')

@login_required
def AcceptExpenses(request, delegacja_id):
    delegacja = get_object_or_404(BusinessTrip, pk=delegacja_id)
    # przechowaj __str__ delegacji i wyślij potem do messages
    if delegacja:
        delegacja.akceptacja_zrealizowanej = True
        delegacja.do_managera = False
        delegacja.save()
        messages.success(request, "Wydatki delegacji " + str(delegacja.id) + " zostały zatwierdzone")
        return redirect('delegacje_do_zatwierdzenia')

@login_required
def DoNotAcceptExpenses(request, delegacja_id):
    delegacja = get_object_or_404(BusinessTrip, pk=delegacja_id)
    # przechowaj __str__ delegacji i wyślij potem do messages
    if delegacja:
        delegacja.akceptacja_zrealizowanej = False  # chociaż pewnie już byłą False
        delegacja.do_managera = False
        delegacja.save()
        messages.success(request, "Wydatki delegacji " + str(delegacja.id) + " zostały cofnięte do pracownika")
        return redirect('delegacje_do_zatwierdzenia')

@login_required
def AcceptBusinessTrip(request, delegacja_id):
    delegacja = get_object_or_404(BusinessTrip, pk=delegacja_id)
    # przechowaj __str__ delegacji i wyślij potem do messages
    if delegacja:
        delegacja.akceptacja_planowanej = True
        delegacja.do_managera = False
        delegacja.save()
        messages.success(request, "Delegacja " + str(delegacja.id) + " została zatwierdzona")
        return redirect('delegacje_do_zatwierdzenia')

@login_required
def DoNotAcceptBusinessTrip(request, delegacja_id):
    delegacja = get_object_or_404(BusinessTrip, pk=delegacja_id)
    # przechowaj __str__ delegacji i wyślij potem do messages
    if delegacja:
        delegacja.akceptacja_planowanej = False
        delegacja.do_managera = False
        delegacja.save()
        messages.success(request, "Delegacja " + str(delegacja.id) + " została cofnięta do pracownika")
        return redirect('delegacje_do_zatwierdzenia')

@login_required
def RequestBusinessTrip(request, delegacja_id):
    delegacja = get_object_or_404(BusinessTrip, pk=delegacja_id)
    # przechowaj __str__ delegacji i wyślij potem do messages
    if delegacja:
        delegacja.do_managera = True
        delegacja.save()
        messages.success(request, "Delegacja została wysłana do kierownika po potwierdzenie")
        return redirect('business_trip_home')

@login_required
def RequestBusinessTripExpenses(request, delegacja_id):
    delegacja = get_object_or_404(BusinessTrip, pk=delegacja_id)
    # przechowaj __str__ delegacji i wyślij potem do messages
    if delegacja:
        delegacja.do_managera = True
        delegacja.save()
        messages.success(request, "Wydatki delegacji " + str(delegacja_id) + " zostały wysłane do kierownika po potwierdzenie")
        return redirect('business_trip_home')

# class BusinessTripView(CreateView):
#     model = BusinessTrip
#     fields = ['kraj', 'miasto', 'poczatek', 'koniec']
#
#     def form_valid(self, form):
#         form.instance.pracownik = self.request.user
#         return super().form_valid(form)

#
# @login_required
# def BusinessTripList(request):
#     delegacje = BusinessTrip.objects.filter(pracownik=request.user)
#
#     return render(request,'moje_delegacje.html')