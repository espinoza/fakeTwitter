import re
from django import forms
from .models import User, Tweet
import bcrypt
from .utils import contains_digit, contains_uppercase

email_regex = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
username_regex = r'^[A-Za-z0-9_]+$'
full_name_regex = r'^[A-Za-z\s]+$'


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Contraseña'}
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirmar contraseña'}
        )
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'full_name']
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Nombre de usuario'}
            ),
            'email': forms.TextInput(
                attrs={'placeholder': 'Correo'}
            ),
            'full_name': forms.TextInput(
                attrs={'placeholder': 'Nombre completo'}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if len(password) < 8:
            raise forms.ValidationError(
                {'password': 'La contraseña debe tener al menos 8 caracteres'}
            )
        if not contains_digit(password):
            raise forms.ValidationError(
                {'password': 'La contraseña debe tener al menos 1 dígito'}
            )
        if not contains_uppercase(password):
            raise forms.ValidationError(
                {'password': 'La contraseña debe tener al menos 1 mayúscula'}
            )
        if password != confirm_password:
            raise forms.ValidationError(
                {'confirm_password': 'Las contraseñas no coinciden'}
            )
        
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if not re.fullmatch(username_regex, username):
            raise forms.ValidationError(
                'Nombre de usuario no válido'
            )
        if user:
            raise forms.ValidationError(
                'El nombre de usuario ya existe'
            )
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.fullmatch(email_regex, email):
            raise forms.ValidationError(
                'Correo no válido'
            )
        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError(
                'El correo ya ha sido ocupado por otro usuario'
            )
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if not re.fullmatch(full_name_regex, full_name):
            raise forms.ValidationError(
                'Solo se permiten letras y espacios'
            )
        return full_name


class LoginForm(forms.Form):

    email_or_username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Correo o nombre de usuario'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Contraseña'}
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        email_or_username = cleaned_data.get('email_or_username')
        password = cleaned_data.get('password')

        user = None

        if '@' in email_or_username:
            if re.fullmatch(email_regex, email_or_username):
                user = User.objects.filter(email=email_or_username)
            else:
                raise forms.ValidationError('Correo no válido')

        else:
            if re.fullmatch(username_regex, email_or_username):
                user = User.objects.filter(username=email_or_username)
            else:
                raise forms.ValidationError('Nombre de usuario no válido')

        if not user:
            raise forms.ValidationError('El usuario no existe')
        user = user[0]

        if not bcrypt.checkpw(password.encode(), user.password_hash.encode()):
            raise forms.ValidationError('Contraseña incorrecta')

        return cleaned_data


class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ['message']
        widgets = {
            'message': forms.Textarea(
                attrs={'placeholder': '¿Qué hay de nuevo?'}
            )
        }
