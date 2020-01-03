from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Scoate username de la required si pune in loc email
AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False
AbstractUser._meta.get_field('username').blank = True
AbstractUser._meta.get_field('username')._unique = False


class UserManager(BaseUserManager):
    #Necesar pentru a scoate username de la required

    def create_user(self, email, password, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


class Utilizator(AbstractUser):
    """ Tabel info utilizator 
        nume            - extras automat din email ([nume]@gmail.com)
        email           - se va loga cu emailul
        parola          - *** 
        descriere       - informatiile despre utilizator scrise de acesta pentru celilati potential colegi de apartament
        ocupatie        - tipul jobului
        sex             - mf
        varsta          - 
        buget           - 
        imagine_profil  - imagine profil
        cont_admin      - are access la backend, administratorul poate gestiona utilizatorii si anunturile
        cont_premium: regular: cont gratis poate avea activ doar un anunt, 
                      premium: cont platit poate avea activ unul sau mai multe anunturi, 
                               poate vedea statistici cu privire la anunturile postate
                               primeste prin email atunci cand un anunt a fost postat

        Un utilizator poate avea unul sau mai multe anunturi postate si/sau unul sau mai multe anunturi salvate la favorite
    """
    email      = models.EmailField(unique=True)
    descriere  = models.CharField(max_length=255, blank=True)
    ocupatie   = models.CharField(max_length=50, blank=True)
    sex        = models.CharField(max_length=1, default="N", blank=True)
    token      = models.CharField(max_length=1, blank=True)
    varsta     = models.PositiveIntegerField(blank=True, null=True)
    buget      = models.PositiveIntegerField(blank=False, null=True)
    imagine_profil  = models.ImageField(blank=True, upload_to="utilizatori/")
    cont_premium    = models.BooleanField(default=False)
    
    #Scoatem field/coloanele 
    first_name = None
    last_name  = None

    #Necesare pentru a inlocui username cu email
    username  = None
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []
    objects   = UserManager()
    
    def __str__(self):
        return f"{self.email}"

    @property
    def nume(self):
        return f"{self.email.split('@')[0]}"

    class Meta:
        verbose_name_plural = "Utilizatori"

    
class Anunt(models.Model):
    """
        Tabel info anunt

        postat_de                - str emailul utilizatorului Foreignkey 
        inchiriere_camera        - str DA camera,  NU apartament sau alteva 
        data_postarii            - date
        localitate               - str iasi, bucuresti etc
        zona                     - str punct de referinta, cartier
        pret                     - int pretul in euro
        numar_camere             - int numarul camerelor libere
        numar_colegi             - int numarul colegilor de apartament/locuinta
        mfx                      - str colegi doar baieti(m), doar fete(f), fete/baieti(x)
        descriere                - str descrierea locuintei in detaliu 
        titlu                    - generat automat din localitate + zona + pret 
        facilitati               - date extrase automat din descriere
        img1                     - prima imagine
        img2                     - a doua imagine etc
       
        Un anunt poate avea unul sau mai multi utilizatori interesati de share (sheriasi)
    """

    postat_de     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_postarii = models.DateTimeField(auto_now_add=True)
    localitate    = models.CharField(max_length=50, blank=False)
    zona          = models.CharField(max_length=100, blank=False)
    pret          = models.PositiveIntegerField(blank=False)
    numar_camere  = models.PositiveIntegerField(blank=False)
    numar_colegi  = models.PositiveIntegerField(blank=False)
    mfx           =  models.CharField(max_length=1, blank=False)
    descriere     = models.TextField(max_length=250, blank=False)    
    img1 = models.ImageField(upload_to="anunturi/")
    img2 = models.ImageField(upload_to="anunturi/", blank=True)
    img3 = models.ImageField(upload_to="anunturi/", blank=True)
    img4 = models.ImageField(upload_to="anunturi/", blank=True)
    img5 = models.ImageField(upload_to="anunturi/", blank=True)
    img6 = models.ImageField(upload_to="anunturi/", blank=True)
    
    facilitati = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.localitate}, {self.zona} - {self.pret}"

    @property
    def titlu(self):
        return f"{self.localitate}, {self.zona}"

    class Meta:
        verbose_name_plural = "Anunturi"

    
    

class Favorite(models.Model):
    """
        Tabel info Favorite

        utilizator - emailul utilizatorului care l-a salvat
        anunt - anuntul pe care l-a salvat        

    """

    utilizator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    anunt = models.ForeignKey('Anunt', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Favorite"




class Sheriasi(models.Model):
    """
        Table info sheriasi

        utilizator -  cel care doreste sa imparta chiria pentru anuntul postat
        anunt      -  anuntul postat
        
        Cand un utilizator este interesat sa imparta chiria pentru un apartament atunci
        o noua linie va fi create in acest tabel ce va contine anuntul in cauza si utilizatorul
    """

    utilizator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    anunt = models.ForeignKey('Anunt', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Sheriasi"



    