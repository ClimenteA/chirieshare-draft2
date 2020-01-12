from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Utilizator, Anunt, Favorite, Sheriasi
from .forms import AutentificareForm, AnuntForm, FavoriteForm, SheriasiForm

from django.conf import settings
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import JsonResponse, HttpResponse
#from django.template.loader import render_to_string 
# #return HttpResponse(render_to_string("detalii_anunt.html", {}))
    


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
            messages.error(request, 'Date de logare incorecte!')
            return render(request, "autentificare.html", {'form': AutentificareForm})


        
def inregistrare(request, activare_cont=None):
    """ Inregistrare si trimitere link activare catre utilizator """

    if request.method == 'GET':

        if activare_cont == None:
            return render(request, "inregistrare.html", {'form': AutentificareForm})
        else:
            # Activare cont
            user = Utilizator.objects.get(pk=int(activare_cont.split("-")[0]))
            if user.token == activare_cont:
                user.is_active = True
                user.token = ""
                user.save()
                messages.success(request, 'Contul a fost activat!')
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
            messages.error(request, 'Emailul introdus este folosit! Ti-ai uitat parola?')
            return redirect('inregistrare')

        activare_cont_id = str(user.pk) + "-" + get_random_string()
        user.is_active = False
        user.token = activare_cont_id
        
        # Trimite link de activare catre mailul utilizatorului
        send_mail("Activare cont chirieshare.ro", 
                f"Salut,\n\nAcceseaza linkul de mai jos pentru a activa contul:\n\nhttp://127.0.0.1:8000/inregistrare/{activare_cont_id}", 
                settings.EMAIL_HOST_USER, 
                [request.POST['email']])
    
        user.save()

        messages.success(request, 'Acceseaza linkul primit prin email pentru activarea contului!')
        return redirect('autentificare')

        
                

def resetare_cont(request, resetare_cont_id=None):
    
    if request.method == 'GET':

        if resetare_cont_id == None:
            return render(request, "resetare_cont.html", {})
        else:
            user = Utilizator.objects.get(pk=int(resetare_cont_id.split("-")[0]))
            
            if user.token == resetare_cont_id:
                user.delete()
                messages.success(request, 'Contul a fost resetat! Introdu noile date de logare!')
                return redirect('inregistrare') 
            else:
                messages.error(request, 'Pagina ceruta nu a fost gasita!')
                return redirect('pagina_de_prezentare')

    if request.method == 'POST':
     
        try: 
            user = Utilizator.objects.get(email=request.POST['email'])
        except:
            messages.error(request, 'Emailul introdus nu exista!')
            return redirect('resetare_cont')

        resetare_cont_id = str(user.pk) + "-" + get_random_string()
        user.token = resetare_cont_id
        
        # Trimite link de activare catre mailul utilizatorului
        send_mail("Resetare cont chirieshare.ro", 
                f"Salut,\n\nAcceseaza linkul de mai jos pentru a reseta contul:\n\nhttp://127.0.0.1:8000/resetare-cont/{resetare_cont_id}", 
                settings.EMAIL_HOST_USER, 
                [request.POST['email']])
    
        user.save()

        messages.error(request, 'Reseteaza contul accesand linkul din emailul primit!')
        return redirect('pagina_de_prezentare')

    

@login_required
def adauga_anunt(request):
    """ Adauga un anunt """

    if request.method == "GET":
        return render(request, "adauga_anunt.html", {})
    
    elif request.method == "POST":
        form = AnuntForm(request.POST, request.FILES, instance=request.user) 
        if form.is_valid():
            Anunt(postat_de=request.user, **form.cleaned_data).save()
            messages.success(request, 'Anuntul a fost adaugat!')
            return render(request, "adauga_anunt.html", {})
        else:
            messages.error(request, 'Datele cerute nu au fost completate corect!')
            return render(request, "adauga_anunt.html", {})
    
    
def anunturi(request, localitate="", zona="", apcam="", pret=""):
    
    anunturi = Anunt.objects.all().order_by('-data_postarii')

    print("Filtre: ", localitate, zona, apcam, pret, type(pret))
    
    if localitate not in ["toate", ""]:
        anunturi = anunturi.filter(localitate__contains=localitate)
    if zona not in ["toate", ""]:
        anunturi = anunturi.filter(zona__contains=zona)
    if pret not in ["0", ""]:
        anunturi = anunturi.filter(pret__lte=int(pret))
    
    # if apcam:
    #     anunturi = anunturi.filter(apartament__contains=apcam)
    
    page = request.GET.get('page', 1)
    paginator = Paginator(anunturi, 15)

    try:
        anunturi_ = paginator.page(page)
    except PageNotAnInteger:
        anunturi_ = paginator.page(1)
    except EmptyPage:
        anunturi_ = paginator.page(paginator.num_pages)


    return render(request, "anunturi.html", {"anunturi": anunturi_, 
                                             "filtre": {"localitate": localitate, 
                                                        "zona":zona, 
                                                        "apcam":apcam, 
                                                        "pret":pret, 
                                                        }})



@login_required
def adauga_la_favorite(request, id_anunt):

    return JsonResponse({"ok": id_anunt})


@login_required
def scoate_de_la_favorite(request, id_anunt):

    return JsonResponse({"ok": id_anunt})



def detalii_anunt(request, id_anunt):
    return render(request, "detalii_anunt.html", {})




@login_required
def cont(request, id_utilizator=None):
    return render(request, "cont.html", {})

@login_required
def actualizare_cont(request, id_utilizator=None):
    return render(request, "actualizare_cont.html", {})
