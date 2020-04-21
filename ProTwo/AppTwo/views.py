from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404


from AppTwo.models import Utente, ContiCorrente, UtenteForm
# Create your views here.


def index(request):
    my_dict = {'inserte_me': 'Questa pagina con ENFASI',
               'altImage': 'Foto di Django'}
    return render(request, 'AppTwo/index.html', context=my_dict)

def index_user(request):
    utenti = Utente.objects.order_by('nome')
    my_dict = {'inserte_me': 'Questa pagina con ENFASI',
               'altImage': 'Foto di Django',
               'utenti':utenti}
    return render(request, 'AppTwo/index_user.html', context=my_dict)

def detailUtente(request, utente_nome):
    utente = get_object_or_404(Utente, nome=utente_nome)
    return render(request, 'AppTwo/detail_user.html', {'utente': utente})

def index_conticorrente(request):
    conti = ContiCorrente.objects.all
    my_dict = {'inserte_me': 'Questa pagina con ENFASI',
               'altImage': 'Foto di Django',
               'conti':conti}
    return render(request, 'AppTwo/index_conti.html', context=my_dict)

def utente_form(request):
    if request.method == 'POST':
        form = UtenteForm(request.POST)
        if form.is_valid():
            #CARICO I DATI NEL DBMS
            print('VALIDATION IS OK')
            print('Nome: ' + form.cleaned_data['nome'])
            print('Email: ' + form.cleaned_data['email'])
            print('Cognome: ' + form.cleaned_data['cognome'])
            form.save(commit=True)
            return index_user(request)
        else:
            print('Errore nella form')
    return render(request, 'appTwo/formUtente.html', {'form':UtenteForm})


def other(request):
    return render(request, 'AppTwo/other.html')

def help(request):
    # return HttpResponse(result)
    my_dict = {'friends': 'Mimmo, Saverio, Luca, Gennaro'}
    return render(request, 'AppTwo/help.html', context=my_dict)
