from django.db import models


class Utilizator(models.Model):
    """ Tabel info utilizator 
        nume            - extras automat din email ([nume]@gmail.com)
        email           - se va loga cu emailul
        parola          - *** 
        descriere       - informatiile despre utilizator scrise de acesta pentru celilati potential colegi de apartament
        tip_cont  - 
            regular: cont gratis poate avea activ doar un anunt, 
            premium: cont platit poate avea activ unul sau mai multe anunturi, 
                            poate vedea statistici cu privire la anunturile postate
                            primeste prin email atunci cand un anunt a fost postat

        Un utilizator poate avea unul sau mai multe anunturi postate si/sau unul sau mai multe anunturi salvate la favorite
    """


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
        img3
        img4

        Un anunt poate avea unul sau mai multi utilizatori interesati de share (sheriasi)
    """
    

class Favorite(models.Model):
    """
        Tabel info Favorite

        email - emailul utilizatorului care l-a salvat
        anunt - anuntul pe care l-a salvat        

    """

class Sheriasi(models.Model):
    """
        Table info sheriasi

        anunt      -  
        utilizator -  
        
        Cand un utilizator este interesat sa imparta chiria pentru un apartament atunci
        o noua linie va fi create in acest tabel ce va contine anuntul in cauza si utilizatorul
    """
    