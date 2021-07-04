from django import forms
from .models import User

class RegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name']

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if user:
            raise forms.ValidationError(
                'El nombre de usuario ya ha sido ocupado por otro usuario'
            )
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError(
                'El correo ya ha sido ocupado por otro usuario'
            )
        return email
