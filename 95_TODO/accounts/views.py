from django.shortcuts import redirect, render
from accounts.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def signup(request):
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


def login(request):
    if request.method=='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }

    return render(request, 'accounts/form.html', context)