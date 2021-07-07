from functools import wraps
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm, LoginForm, TweetForm
from .models import User, Login, Tweet
import bcrypt
from django.http import JsonResponse


def login_required(view):
    """Decorator to redirect to login when there is not logged user."""
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('login')
        user = User.objects.filter(id=request.session['user_id'])
        if not user:
            return redirect('login')
        logged_user = user[0]
        return view(request, logged_user, *args, **kwargs)
    return wrapper


def redirect_if_logged(view):
    """Decorator to redirect to login when there is not logged user."""
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if 'user_id' in request.session:
            user = User.objects.filter(id=request.session['user_id'])
            if user:
                return redirect('home')
        return view(request, *args, **kwargs)
    return wrapper


def index(request):
    return redirect('home')


@redirect_if_logged
def register(request):
    """User registration form view."""
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


@redirect_if_logged
def login(request):
    """User login form view.
    Email or username can be used on the same field.
    """
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
    """User logout view."""
    del request.session['user_id']
    return redirect('login')


@login_required
def home(request, logged_user):
    """Main page with a list of tweets and a form to post a new tweet."""

    if request.method == 'POST':
        message = request.POST["message"]
        form = TweetForm(
            data={
                "message": message,
            }
        )

        created_at = None

        if form.is_valid():
            new_tweet = Tweet.objects.create(
                message=message, user=logged_user
            )

        return JsonResponse({
            "message": message,
            "userFullName": logged_user.full_name,
            "username": logged_user.username,
            "created_at": new_tweet.formatted_created_at,
            "errors": form.errors,
        })

    form = TweetForm()
    tweets = Tweet.objects.all().order_by('-created_at')
    user_last_tweet = Tweet.objects.filter(user=logged_user).last()
    user_last_logins = Login.objects.filter(user=logged_user) \
                                    .order_by("-datetime")[:10]

    return render(request, template_name='home.html',
                  context={
                      'form': form,
                      'tweets': tweets,
                      'user_last_tweet': user_last_tweet,
                      'user_last_logins': user_last_logins,
                      'user': logged_user,
                  })

