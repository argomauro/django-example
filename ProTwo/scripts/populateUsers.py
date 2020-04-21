import os
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent
sys.path.append(str(PROJECT_ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from AppTwo.models import Utente, ContiCorrente
from faker import Faker

fake = Faker()

def addUtente():
    utente = Utente.objects.get_or_create(nome=fake.first_name(),
    cognome=fake.last_name(),
    email=fake.email(),
    data_registrazione=fake.past_datetime())[0]
    utente.save()

    contoCorrente = ContiCorrente.objects.get_or_create(utente=utente,
    nomeBanca=fake.company(),
    iban=fake.iban())[0]
    contoCorrente.save()

    return utente



def populate(N=5):
    for entry in range(N):
        utente = addUtente()
        print(utente.__str__())



def run():
    print("Populating the databases Users...Please Wait")
    populate(20)
    print('Populating Complete')
