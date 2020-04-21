# Generated by Django 3.0.3 on 2020-04-08 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cognome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('data_registrazione', models.DateTimeField(verbose_name='data registrazione')),
            ],
        ),
        migrations.CreateModel(
            name='ContiCorrente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeBanca', models.CharField(max_length=200)),
                ('iban', models.CharField(max_length=200)),
                ('utente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppTwo.Utente')),
            ],
        ),
    ]
