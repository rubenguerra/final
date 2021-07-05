from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields} #iteramos entre los campos para poner strings vacíos


class FormBuscar(forms.Form):
    buscar = forms.CharField(required=False, min_length=3)
    buscar_en = forms.ChoiceField(required=False, choices=(('producto', 'Producto'),
                                                           ('categoria', 'Categoria')))
