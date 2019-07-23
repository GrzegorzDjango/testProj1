from django.urls import path
from . import views

urlpatterns = [
    path('moje', views.BusinessTripHome, name='business_trip_home'),
    path('ukonczone', views.BusinessTripDone, name='business_trip_done'),
    path('nowa', views.BusinessTripCreate, name='nowa_delegacja'),
    path('<int:delegacja_id>', views.BusinessTripPrepare, name='wypelnij_delegacje'),
    path('<int:delegacja_id>/planned_payment/<int:payment_id>/del', views.DeletePayment, name='usun_wydatek'),
    path('<int:delegacja_id>/realized_payment/<int:realized_payment_id>/del', views.DeleteRealizedPayment, name='usun_zrealizowany_wydatek'),
    path('<int:delegacja_id>/del', views.DeleteBusinessTrip, name='usun_delegacje'),

    path('<int:delegacja_id>/zaksieguj_delegacje', views.BookBusinessTrip, name='zaksieguj_delegacje'),  # ten 1
    path('<int:delegacja_id>/<int:wydatek_id>/zaksieguj_wydatek', views.BookExpense, name='zaksieguj_wydatek'), # ten 2

    path('<int:delegacja_id>/zatwierdz_wydatki', views.AcceptExpenses, name='zatwierdz_wydatki'),
    path('<int:delegacja_id>/cofnij_wydatki', views.DoNotAcceptExpenses, name='cofnij_wydatki'),

    path('<int:delegacja_id>/zatwierdz_delegacje', views.AcceptBusinessTrip, name='zatwierdz_delegacje'),
    path('<int:delegacja_id>/cofnij_delegacje', views.DoNotAcceptBusinessTrip, name='cofnij_delegacje'),

    path('<int:delegacja_id>/wnioskuj_delegacje', views.RequestBusinessTrip, name='wnioskuj_delegacje'),
    path('<int:delegacja_id>/wnioskuj_wydatki', views.RequestBusinessTripExpenses, name='wnioskuj_wydatki'),
    path('do_zatwierdzenia', views.BusinessTripsAndExpensesToAccept, name='delegacje_do_zatwierdzenia'),
    path('do_zaksiegowania', views.BusinessTripsAndExpensesToBook, name='delegacje_do_zaksiegowania'),
    path('zaksiegowane', views.BusinessTripsAndExpensesBooked, name='delegacje_zaksiegowane'),


]

