# Generated by Django 2.2 on 2019-05-22 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delegacja', '0015_auto_20190522_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realizedexpense',
            name='dokument1',
            field=models.FileField(blank=True, upload_to='faktury/'),
        ),
    ]