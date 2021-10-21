from django.shortcuts import redirect, render, get_object_or_404
from .forms import CustonUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustonUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustonUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/form.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('accounts:profile', user.username)
    else:
        form = AuthenticationForm()
        
    context = {
        'form':form
    }
    return render(request, 'accounts/form.html', context)


def profile(request, username):
    User = get_user_model() # 클래스
    profile_user = get_object_or_404(User, username=username) # 단일 인스턴스

    context = {
        'profile_user' : profile_user
    }

    return render(request, 'accounts/profile.html', context)


def follow(request, pk):
    User = get_user_model()
    # me = 로그인한 사람, 팔로우 버튼을 누른 사람
    me = request.user
    # you = 내가 프로필 페이지를 보고 있는 사람, 팔로우 할 사람
    you = get_object_or_404(User, pk=pk)

    if me in you.followers.all():
        me.followings.remove(you)
    else:
        # you.followers.add(me)
        me.followings.add(you)
    return redirect('accounts:profile', you.username)