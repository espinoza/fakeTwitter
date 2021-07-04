from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm, LoginForm, TweetForm
from .models import User, Login, Tweet
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
            Login.objects.create(user=new_user)
            request.session['user_id'] = new_user.id

            return redirect('home')

    return render(request, template_name='register.html',
                  context={'form': form})


def login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email_or_username = request.POST['email_or_username']
            if '@' in email_or_username:
                user = User.objects.get(email=email_or_username)
            else:
                user = User.objects.get(username=email_or_username)
            request.session['user_id'] = user.id
            Login.objects.create(user=user)
            return redirect('home')

    return render(request, template_name='login.html',
                  context={'form': form})


def logout(request):
    del request.session['user_id']
    return redirect('login')


def home(request):
    if 'user_id' not in request.session:
        return redirect('login')
    user = User.objects.filter(id=request.session['user_id'])
    if not user:
        return redirect('login')
    logged_user = user[0]

    form = TweetForm()

    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.user = logged_user
            new_tweet.save()
            return redirect('home')

    tweets = Tweet.objects.all().order_by('-created_at')

    return render(request, template_name='home.html',
                  context={'form': form, 'tweets': tweets})


