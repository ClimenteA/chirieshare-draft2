"""chirieshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from website import views

urlpatterns = [
    # path('/', views.pagina_de_prezentare, name="pagina_de_prezentare"),
    path('inregistrare-cont/', views.inregistrare_cont, name="inregistrare_cont"),
    path('autentificare/', views.autentificare, name="autentificare"),
    # path('resetare-parola/', views.resetare_parola, name="resetare_parola"),
    # path('adauga-anunt/', views.adauga_anunt, name="adauga_anunt"),
    # path('anunturi/<localitate>/<zona>/<pret>/<camera>/<apartament>/', views.anunturi, name="anunturi"),
    # path('detalii-anunt/<id_anunt>/', views.detalii_anunt, name="detalii_anunt"),
    # path('cont/<utilizator>/', views.utilizator, name="utilizator"),
    # path('modificare-cont/<utilizator>', views.modificare_utilizator, name="modificare_utilizator"),

    path('admin/', admin.site.urls),
]
