from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Country, Currency, Project, Employee, PaymentType, FinalPaymentType, ExpenseType


#class PracownikAdmin(admin.ModelAdmin):
#    list_display = ('id', 'pracownik', 'projekt',)
#    search_fields = ('pracownik',)
#    list_filter = ('projekt',)
#    list_per_page = 25
#
#admin.site.register(Pracownik, PracownikAdmin)

######### poniżej dodajemy do adminu zmodyfikowanego pracownika #########
# https://subscription.packtpub.com/book/application_development/9781787281141/11/ch11lvl1sec96/extending-the-existing-user-model

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'Pracownicy'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

######### koniec modyfikowania pracownika #################################

class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'kraj', 'waluta', 'dzienna_kwota')
    list_editable = ('waluta', 'dzienna_kwota')
    list_filter = ('waluta', )
    search_fields = ('kraj', )
    list_per_page = 25

admin.site.register(Country, CountryAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'waluta')
    search_fields = ('waluta',)
    list_per_page = 25

admin.site.register(Currency, CurrencyAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'projekt', 'kierownik')
    search_fields = ('projekt',)
    list_filter = ('kierownik',)
    list_per_page = 25

admin.site.register(Project, ProjectAdmin)


class ExpenseTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExpenseType, ExpenseTypeAdmin)


class PaymentTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(PaymentType, PaymentTypeAdmin)


class FinalPaymentTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(FinalPaymentType, FinalPaymentTypeAdmin)
