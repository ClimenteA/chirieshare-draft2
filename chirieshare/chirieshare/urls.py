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
    path('', views.pagina_de_prezentare, name="pagina_de_prezentare"),
    path('autentificare/', views.autentificare, name="autentificare"),
    path('inregistrare/', views.inregistrare, name="inregistrare"),
    path('inregistrare/<activare_cont>/', views.inregistrare, name="inregistrare"),
    path('resetare-cont/', views.resetare_cont, name="resetare_cont"),
    path('resetare-cont/<resetare_cont_id>/', views.resetare_cont, name="resetare_cont"),
    path('adauga-anunt/', views.adauga_anunt, name="adauga_anunt"),
    path('anunturi/', views.anunturi, name="anunturi"),
    path('anunturi/<localitate>/<zona>/<pret>/<camera>/<apartament>/', views.anunturi, name="anunturi"),
    path('detalii-anunt/<id_anunt>/', views.detalii_anunt, name="detalii_anunt"),
    path('cont/', views.cont, name="cont"),
    path('cont/<id_utilizator>/', views.cont, name="cont"),
    path('actualizare-cont/', views.actualizare_cont, name="actualizare_cont"),
    path('actualizare-cont/<id_utilizator>/', views.actualizare_cont, name="actualizare_cont"),

    path('admin/', admin.site.urls),
]


#Serving images during dev
from django.conf import settings 

if settings.DEBUG:
    from django.conf.urls.static import static
    #this line makes images from media folder available via url media/imgname.png
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
