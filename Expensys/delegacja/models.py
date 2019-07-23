from django.db import models
# from datetime import datetime
from django.contrib.auth.models import User
from pierdoly.models import Country, Currency, ExpenseType, PaymentType, FinalPaymentType, Employee
import datetime

class BusinessTrip(models.Model):
    pracownik = models.ForeignKey(User, on_delete=models.CASCADE)
    kraj = models.ForeignKey(Country, on_delete=models.CASCADE)
    miasto = models.CharField(max_length=30)
    data_wniosku = models.DateTimeField(auto_now_add=True)
    poczatek = models.DateTimeField()
    koniec = models.DateTimeField()
    akceptacja_planowanej = models.BooleanField(default=False)
    akceptacja_zrealizowanej = models.BooleanField(default=False)
    delegacja_zaksiegowana = models.BooleanField(default=False)
    do_managera = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + " | " + self.pracownik.username + " | " + self.kraj.kraj + \
               " | " +self.miasto + " | " + str(self.poczatek)[:10]

    class Meta:
        # verbose_name - tego nie bo Django i tak by dodało s na końcu
        ordering = ('-poczatek',)
        verbose_name_plural = "Delegacje"


class PlannedExpense(models.Model):
    delegacja = models.ForeignKey(BusinessTrip, on_delete=models.CASCADE)
    rodzaj_wydatku = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    rodzaj_platnosci = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    kwota = models.DecimalField(max_digits=6, decimal_places=2)
    waluta = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return self.rodzaj_wydatku.wydatek + " | " + str(self.kwota)

    class Meta:
        # verbose_name - tego nie bo Django i tak by dodało s na końcu
        verbose_name_plural = "Planowane wydatki"

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'faktury/{0}/{1}'.format(instance.delegacja.id, filename)

class RealizedExpense(models.Model):
    delegacja = models.ForeignKey(BusinessTrip, on_delete=models.CASCADE)
    rodzaj_wydatku = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    rodzaj_zrealizowanej_platnosci = models.ForeignKey(FinalPaymentType, on_delete=models.CASCADE)
    kwota = models.DecimalField(max_digits=6, decimal_places=2)
    waluta = models.ForeignKey(Currency, on_delete=models.CASCADE)
    dokument1 = models.FileField(upload_to=user_directory_path, blank=True)
    dokument2 = models.FileField(upload_to=user_directory_path, blank=True)
    dokument3 = models.FileField(upload_to=user_directory_path, blank=True)
    wydatek_zaksiegowany = models.BooleanField(default=False)
    # def dokument1(self):
    #     return models.ImageField(upload_to='faktury/' + self.delegacja.pk)
    #
    # def dokument2(self):
    #     return models.ImageField(upload_to='faktury/' + self.delegacja.pk)
    #
    # def dokument3(self):
    #     return models.ImageField(upload_to='faktury/' + self.delegacja.pk)
    #
    # # trik żeby móc ładować do dokumenty do folderów dotycznących delegacji w której jesteśmy
    # def save(self, *args, **kwargs):
    #     if not self.dokument1:
    #         self.dokument1 = self.dokument1()
    #     if not self.dokument2:
    #         self.dokument2 = self.dokument2()
    #     if not self.dokument1:
    #         self.dokument3 = self.dokument3()
    #     super(RealizedExpense, self).save(*args, **kwargs)

    def __str__(self):
        return self.rodzaj_wydatku.wydatek + " | " + str(self.kwota)

    class Meta:
        # verbose_name - tego nie bo Django i tak by dodało s na końcu
        verbose_name_plural = "Zrealizowane wydatki"


class StayAbroad(models.Model):
    delegacja = models.ForeignKey(BusinessTrip, on_delete=models.CASCADE)
    kraj = models.ForeignKey(Country, on_delete=models.CASCADE)
    poczatek = models.DateTimeField()
    koniec = models.DateTimeField()

    def __str__(self):
        return self.kraj.kraj + " | " + str(self.poczatek)[:10] + " - " + str(self.koniec)[:10]

    class Meta:
        # verbose_name - tego nie bo Django i tak by dodało s na końcu
        verbose_name_plural = "Pobyt zagranicą"