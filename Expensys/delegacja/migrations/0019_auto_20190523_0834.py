# Generated by Django 2.2 on 2019-05-23 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delegacja', '0018_auto_20190523_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstrip',
            name='koniec',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='businesstrip',
            name='poczatek',
            field=models.DateTimeField(),
        ),
    ]
