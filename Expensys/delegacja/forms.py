from django import forms
from .models import BusinessTrip, PlannedExpense, RealizedExpense


class BusinessTripForm(forms.ModelForm):

    class Meta:
        model = BusinessTrip
        fields = ['kraj', 'miasto', 'poczatek', 'koniec']
        widgets = {
            'poczatek': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'koniec': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class PlannedExpenseForm(forms.ModelForm):

    class Meta:
        model = PlannedExpense
        fields = ['rodzaj_wydatku', 'rodzaj_platnosci', 'kwota', 'waluta']
        # fields = ['delegacja', 'rodzaj_wydatku', 'rodzaj_platnosci', 'kwota', 'waluta']


class RealizedExpenseForm(forms.ModelForm):

    class Meta:
        model = RealizedExpense
        fields = ['rodzaj_wydatku', 'rodzaj_zrealizowanej_platnosci', 'kwota', 'waluta', 'dokument1', 'dokument2', 'dokument3']
        # fields = ['delegacja', 'rodzaj_wydatku', 'rodzaj_platnosci', 'kwota', 'waluta']