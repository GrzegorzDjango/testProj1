from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    waluta = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.waluta

    class Meta:
        # verbose_name - tego nie bo Django i tak by dodało s na końcu
        verbose_name_plural = "Waluty"


class Country(models.Model):
    kraj = models.CharField(max_length=20)
    waluta = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)
    dzienna_kwota = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.kraj

    class Meta:
        verbose_name_plural = "Kraje"


class ExpenseType(models.Model):
    wydatek = models.CharField(max_length=40)

    def __str__(self):
        return self.wydatek

    class Meta:
        verbose_name_plural = "Rodzaje wydatków"


class PaymentType(models.Model):
    sposob_platnosci = models.CharField(max_length=40)

    def __str__(self):
        return self.sposob_platnosci

    class Meta:
        verbose_name_plural = "Rodzaje płatności"


class FinalPaymentType(models.Model):
    sposob_zrealizowanej_platnosci = models.CharField(max_length=40)

    def __str__(self):
        return self.sposob_zrealizowanej_platnosci

    class Meta:
        verbose_name_plural = "Rodzaje ostatecznych płatności"



class Employee(models.Model):
    pracownik = models.OneToOneField(User, on_delete=models.CASCADE)
    # Projekt w cudzysłowie bo jeszcze nie jest zdefiniowany
    projekt = models.ForeignKey('Project', blank=True, null=True, on_delete=models.SET_NULL)
    # foreign key do siebie samego, manager też jest pracownikiem
    manager = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.pracownik.username

    class Meta:
        verbose_name_plural = "Pracownicy"


class Project(models.Model):
    projekt = models.CharField(max_length=100)
    kierownik = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.projekt

    class Meta:
        verbose_name_plural = "Projekty"


"""
class Kierownik(models.Model):
    kierownik = models.ForeignKey(User, on_delete=models.CASCADE)
    # Projekt w cudzysłowie bo jeszcze nie jest zdefiniowany
    #projekt = models.ForeignKey(Projekt, on_delete=models.CASCADE)

    def __str__(self):
        return self.kierownik1

    class Meta:
        verbose_name_plural = "Kierownicy"
"""











