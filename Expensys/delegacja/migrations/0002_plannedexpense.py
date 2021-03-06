# Generated by Django 2.2 on 2019-05-09 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pierdoly', '0002_expensetype_paymenttype'),
        ('delegacja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlannedExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kwota', models.DecimalField(decimal_places=2, max_digits=6)),
                ('delegacja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delegacja.BusinessTrip')),
                ('rodzaj_platnosci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pierdoly.PaymentType')),
                ('rodzaj_wydatku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pierdoly.ExpenseType')),
                ('waluta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pierdoly.Currency')),
            ],
            options={
                'verbose_name_plural': 'Planowane wydatki',
            },
        ),
    ]
