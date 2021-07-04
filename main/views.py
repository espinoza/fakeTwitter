from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from .models import User
import bcrypt

def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            password = request.POST['password']
            password_hash = bcrypt.hashpw(
                password.encode(), bcrypt.gensalt()
            ).decode()
            new_user.password_hash = password_hash
            new_user.save()
            return redirect('home')

    return render(request, template_name='register.html',
                  context={'form': form})


def login(request):
    pass


def home(request):
    return HttpResponse("ok")
