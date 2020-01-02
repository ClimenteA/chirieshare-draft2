from django.shortcuts import render, redirect, HttpResponse
from .forms import AutentificareForm, AnuntForm, FavoriteForm, SheriasiForm
from django.contrib.auth import authenticate, login
from .models import Utilizator, Anunt, Favorite, Sheriasi

from django.conf import settings
from django.core.mail import send_mail


def pagina_de_prezentare(request):
    return render(request, "pagina_de_prezentare.html", {})


def autentificare(request):
    """ Auth si login utilizator """

    if request.method == 'GET':
        return render(request, "autentificare.html", {'form': AutentificareForm})
    elif request.method == 'POST':
        user = authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('anunturi')
        else:
            # arata un popup de msg de erroare
            return render(request, "autentificare.html", {'form': AutentificareForm})


        
def inregistrare(request):
    """ Inregistrare si login utilizator """

    if request.method == 'GET':
        return render(request, "inregistrare.html", {'form': AutentificareForm})
    elif request.method == 'POST':
        
        user = authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('anunturi')
        else:
            # arata un popup de msg de erroare
            return render(request, "inregistrare.html", {'form': AutentificareForm})


def test_email(request):
    send_mail("subj", "message", settings.EMAIL_HOST_USER, ["climente.alin@gmail.com"])
    return HttpResponse("Mail trimis")


def resetare_parola(request):
    return render(request, "resetare_parola.html", {})

def adauga_anunt(request):
    return render(request, "adauga_anunt.html", {})

def anunturi(request):
    return render(request, "anunturi.html", {})
    
def detalii_anunt(request, id_anunt):
    return render(request, "detalii_anunt.html", {})

def cont(request, id_utilizator=None):
    return render(request, "cont.html", {})

def actualizare_cont(request, id_utilizator=None):
    return render(request, "actualizare_cont.html", {})
