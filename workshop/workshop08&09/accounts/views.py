from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from .forms import CustomUserChangeForm
# Create your views here.

def index(request):
    users = User.objects.all()
    context = {
        'users' : users
    }

    return render(request, 'accounts/index.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context= {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # form.save()
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')


            # return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')



def profile(request, username):
    user = User.objects.get(username=username)

    context = {
        'user' : user
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def delete(request):
    request.user.delete()
    return redirect('accounts:login')


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)



def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form' : form
    }
    return render(request, 'accounts/password.html', context)