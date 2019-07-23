from django.contrib import admin
from .models import BusinessTrip, PlannedExpense, RealizedExpense, StayAbroad


class BusinessTripAdmin(admin.ModelAdmin):
    list_display = ('id', 'pracownik', 'kraj', 'miasto', 'poczatek', 'koniec', 'akceptacja_planowanej', 'akceptacja_zrealizowanej')
    list_filter = ('pracownik', 'kraj' )
    search_fields = ('pracownik', 'kraj', 'miasto',)
    list_per_page = 25


admin.site.register(BusinessTrip, BusinessTripAdmin)


class PlannedExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'delegacja', 'rodzaj_wydatku', 'rodzaj_platnosci', 'kwota', 'waluta')
    list_filter = ('rodzaj_wydatku', 'rodzaj_platnosci', )
    search_fields = ('delegacja', )
    list_per_page = 25


admin.site.register(PlannedExpense, PlannedExpenseAdmin)


class RealizedExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'delegacja', 'rodzaj_wydatku', 'rodzaj_zrealizowanej_platnosci', 'kwota', 'waluta')
    list_filter = ('rodzaj_wydatku', 'rodzaj_zrealizowanej_platnosci', )
    search_fields = ('delegacja', )
    list_per_page = 25


admin.site.register(RealizedExpense, RealizedExpenseAdmin)


class StayAbroadAdmin(admin.ModelAdmin):
    list_display = ('id', 'delegacja', 'kraj', 'poczatek', 'koniec', )
    list_filter = ('delegacja', )
    search_fields = ('delegacja', 'kraj', )
    list_per_page = 25


admin.site.register(StayAbroad, StayAbroadAdmin)