from django.db import models
from django.forms import ModelForm
from django.core import validators
from django.core.exceptions import ValidationError
from datetime import datetime




class Utente(models.Model):
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, validators=[validators.EmailValidator])
    data_registrazione = models.DateTimeField(null=True, blank=True, default=datetime.now)

    def set_data_registrazione(self,data_registrazione):
        self.data_registrazione = data_registrazione

    def __str__(self):
        toString = self.nome + ',' + self.cognome + ',' + self.email
        return  toString



#CLASSE FORM DAL MODELLO UTENTE
class UtenteForm(ModelForm):
    class Meta:
        model = Utente
        exclude = ['data_registrazione']
        #fields = '__all__'

class ContiCorrente(models.Model):
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    nomeBanca = models.CharField(max_length=200)
    iban = models.CharField(max_length=200)

    def __str__(self):
        toString = self.utente.__str__() + ',\n' + self.nomeBanca + ',' + self.iban
        return  toString
