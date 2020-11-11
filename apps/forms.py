from django import forms
from .models import Contacto,Juego
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = '__all__'

        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email","password1","password2"]


