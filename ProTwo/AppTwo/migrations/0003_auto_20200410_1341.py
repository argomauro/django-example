# Generated by Django 3.0.3 on 2020-04-10 11:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0002_auto_20200409_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utente',
            name='data_registrazione',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='utente',
            name='email',
            field=models.EmailField(max_length=100, validators=[django.core.validators.EmailValidator]),
        ),
    ]
