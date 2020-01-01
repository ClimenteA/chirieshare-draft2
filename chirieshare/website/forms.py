# https://docs.djangoproject.com/en/3.0/ref/forms/models/#django.forms.models.modelform_factory
from django.forms import modelform_factory, PasswordInput
from .models import Utilizator, Anunt, Favorite, Sheriasi


AutentificareForm = modelform_factory(Utilizator, fields=['email', 'password'], 
                                                  widgets={'password': PasswordInput})

AnuntForm      = modelform_factory(Anunt,      fields='__all__')
FavoriteForm   = modelform_factory(Favorite,   fields='__all__')
SheriasiForm   = modelform_factory(Sheriasi,   fields='__all__')

