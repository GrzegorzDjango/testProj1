# Generated by Django 2.2 on 2019-05-23 11:13

import delegacja.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delegacja', '0019_auto_20190523_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstrip',
            name='delegacja_zaksiegowana',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='realizedexpense',
            name='wydatek_zaksiegowany',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='realizedexpense',
            name='dokument1',
            field=models.FileField(blank=True, upload_to=delegacja.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='realizedexpense',
            name='dokument2',
            field=models.FileField(blank=True, upload_to=delegacja.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='realizedexpense',
            name='dokument3',
            field=models.FileField(blank=True, upload_to=delegacja.models.user_directory_path),
        ),
    ]