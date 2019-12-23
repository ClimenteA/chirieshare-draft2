from django.shortcuts import render



def autentificare(request):
    return render(request, "autentificare.html", {})

def inregistrare_cont(request):
    return render(request, "autentificare.html", {})
