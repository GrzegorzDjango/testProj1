# Generated by Django 2.2 on 2019-05-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delegacja', '0005_auto_20190519_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='realizedexpense',
            name='akceptacja_planowanej',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='realizedexpense',
            name='akceptacja_zrealizowanej',
            field=models.BooleanField(default=False),
        ),
    ]