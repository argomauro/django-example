from django.shortcuts import render , reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.db import IntegrityError, transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from login.forms import UserForm, UserProfileInfoForm

def index(request):
    return render(request, 'login/index.html')

@login_required
def special(request):
    return HttpResponse('Bravo sei autenticato')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('login:index'))
            else:
                return HttpResponse('Account non attivo')
        else:
            print('Login fallito')
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse('Riprova')
    else:
        return render(request, 'login/login.html',{})

@transaction.atomic
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_Form = UserProfileInfoForm(data=request.POST)


        if user_form.is_valid() and profile_Form.is_valid():
            user = user_form.save(commit=False)
            #user.set_password(user.password())
            print('Password che arriva dentro User: ' + user.password)
            user.password = make_password(password=str(user.password),
                                  salt=None,
                                  hasher='argon2')
            #user.set_password(user_form.cleaned_data["password"])


            profile = profile_Form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            #SALVO CONTESTUALMENTE I DUE OGGETTI PER FARE UNA TRANSAZIONE
            try:
                with transaction.atomic():
                    user.save()
                    profile.save()
            except IntegrityError:
                print('Errore di integrità nel salvataggio')

            registered = True
        else:
            print(user_form.errors, profile_Form.errors)
    else:
        user_form = UserForm()
        profile_Form = UserProfileInfoForm()

    return render(request, 'login/registration.html',
                    {'user_form':user_form,
                    'profile_form':profile_Form,
                    'registered':registered})
