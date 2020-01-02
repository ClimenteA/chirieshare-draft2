from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .models import Utilizator, Anunt, Favorite, Sheriasi
from .forms import AutentificareForm, AnuntForm, FavoriteForm, SheriasiForm

from django.conf import settings
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from django.contrib.auth.decorators import login_required
from django.contrib import messages




def pagina_de_prezentare(request):
    return render(request, "pagina_de_prezentare.html", {})


def autentificare(request):
    """ Auth si login utilizator """

    if request.method == 'GET':
        return render(request, "autentificare.html", {'form': AutentificareForm})
    elif request.method == 'POST':
        user = authenticate(email    = request.POST['email'], 
                            password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('anunturi')
        else:
            messages.error(request, 'Emailul sau parola nu au fost gasite!')
            return render(request, "autentificare.html", {'form': AutentificareForm})


        
def inregistrare(request, activare_cont=None):
    """ Inregistrare si trimitere link activare catre utilizator """

    if request.method == 'GET':

        if activare_cont == None:
            return render(request, "inregistrare.html", {'form': AutentificareForm})
        else:
            # Activare cont
            user = Utilizator.objects.get(pk=int(activare_cont.split("-")[0]))
            if user.descriere == activare_cont:
                user.is_active = True
                user.descriere = ""
                user.save()
                messages.success(request, 'Contul a fost activat cu success!')
                return redirect('autentificare') 
            else:
                messages.error(request, 'Contul nu a putut fi activat!')
                return redirect('inregistrare')

    elif request.method == 'POST':
        # Adauga utilizatorul in baza de date ca inactiv 
        try:
            user = Utilizator.objects.create_user( email    = request.POST['email'], 
                                                   password = request.POST['password'])
        except:
            messages.error(request, 'Emailul introdus este folosit! Reseteaza parola accesand linkul din emailul primit!')
            return redirect('pagina_de_prezentare')

        activare_cont_id = str(user.pk) + "-" + get_random_string()
        user.is_active = False
        user.descriere = activare_cont_id
        
        # Trimite link de activare catre mailul utilizatorului
        send_mail("Activare cont chirieshare.ro", 
                  f"Salut,\n\nAcceseaza linkul de mai jos pentru a activa contul:\n\nhttp://127.0.0.1:8000/inregistrare/{activare_cont_id}", 
                  settings.EMAIL_HOST_USER, 
                  [request.POST['email']])
    
        user.save()

        messages.success(request, 'Acceseaza linkul de activare primit in email pentru activarea contului!')
        return redirect('pagina_de_prezentare')

        

def resetare_parola(request):
    return render(request, "resetare_parola.html", {})

@login_required
def adauga_anunt(request):
    return render(request, "adauga_anunt.html", {})

def anunturi(request):
    return render(request, "anunturi.html", {})
    
def detalii_anunt(request, id_anunt):
    return render(request, "detalii_anunt.html", {})

@login_required
def cont(request, id_utilizator=None):
    return render(request, "cont.html", {})

@login_required
def actualizare_cont(request, id_utilizator=None):
    return render(request, "actualizare_cont.html", {})
