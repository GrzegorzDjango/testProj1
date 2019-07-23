# Generated by Django 2.2 on 2019-05-22 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delegacja', '0009_auto_20190521_1055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businesstrip',
            options={'ordering': ('-poczatek',), 'verbose_name_plural': 'Delegacje'},
        ),
        migrations.AddField(
            model_name='businesstrip',
            name='realizacja_księgowość',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='businesstrip',
            name='pracownik',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
