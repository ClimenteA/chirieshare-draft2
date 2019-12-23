from django.shortcuts import render


def pagina_de_prezentare(request):
    return render(request, "pagina_de_prezentare.html", {})

def autentificare(request):
    return render(request, "autentificare.html", {})

def inregistrare(request):
    return render(request, "inregistrare.html", {})

def resetare_parola(request):
    return render(request, "resetare_parola.html", {})

def adauga_anunt(request):
    return render(request, "adauga_anunt.html", {})

def anunturi(request):
    return render(request, "anunturi.html", {})
    
def detalii_anunt(request, id_anunt):
    return render(request, "detalii_anunt.html", {})

def utilizator(request, id_utilizator):
    return render(request, "utilizator.html", {})
