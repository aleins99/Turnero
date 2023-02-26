from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}), label='Correo electrónico')

    def __init__(self, *args, **kwargs):
        """
        The function takes in a list of fields and a list of widgets, and re>
        the widgets replaced
        """
        super(LoginForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        """
        The function takes in a list of fields and a list of widgets, and re>
        the widgets replaced
        """
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class SolicitarTurnoForm(forms.ModelForm):
    class Meta:
        model = Atencion
        labels = {'ci': 'Cedula de Identidad', 'prioridad': 'Condición', 'espcialidad': 'Servicios'}
        exclude = ["horario_atencion"]

    def __init__(self, *args, **kwargs):
        """
        The function takes in a list of fields and a list of widgets, and re>
        the widgets replaced
        """
        super(SolicitarTurnoForm, self).__init__(*args, **kwargs)
        self.fields['ci'].widget.attrs['placeholder'] = 'Ej: 231345'
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class RegistrarPersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
        exclude = ('fecha_insercion', 'usuario_insercion', 'usuario_modificacion', 'fecha_modificacion', 'activo')

    def __init__(self, *args, **kwargs):
        """
        The function takes in a list of fields and a list of widgets, and re>
        the widgets replaced
        """
        super(RegistrarPersonaForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print(name)
            if name == 'activo':
                field.widget.attrs.update({'type': 'checkbox'})
            elif 'fecha' in name:
                print("entra")
                self.fields[name].widget.input_type = 'date'
                field.widget.attrs.update({'class': 'form-control'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
