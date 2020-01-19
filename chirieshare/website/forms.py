# https://docs.djangoproject.com/en/3.0/ref/forms/models/#django.forms.models.modelform_factory
from django.forms import (modelform_factory, 
                          PasswordInput, 
                          HiddenInput
                         )
from .models import Utilizator, Anunt, Favorite, Sheriasi


AutentificareForm = modelform_factory(Utilizator, fields=['email', 'password'], 
                                                  widgets={'password': PasswordInput})

AnuntForm = modelform_factory(Anunt,fields=['localitate', 
                                            'zona',
                                            'pret',
                                            'numar_camere',
                                            'numar_colegi',
                                            'apartament',
                                            'mfx',
                                            'descriere',
                                            'img1',
                                            'img2',
                                            'img3',
                                            'img4',
                                            'img5',
                                            'img6',
                                            'alte_detalii'],

                                    widgets={'apartament': HiddenInput}    
                                    )
                                            
FavoriteForm   = modelform_factory(Favorite,   fields='__all__')
SheriasiForm   = modelform_factory(Sheriasi,   fields='__all__')

