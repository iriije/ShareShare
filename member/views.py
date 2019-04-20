from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from .forms import ShareeSignupForm, SharerSignupForm, LoginForm


def login(request):
    if request.method == 'POST':
        next = request.GET.get('next')
        login_form = LoginForm(request=request, data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            django_login(request, user)
            return redirect(next if next else 'index')
        login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다.')
    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form,
    }
    return render(request, 'member/login.html', context)



def logout(request):
    django_logout(request)
    return redirect('index')


def signup(request):
    return render(request, 'member/signup.html')


def signupSharee(request):
    if request.method == 'POST':
        signup_form = ShareeSignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            django_login(request, user)
            return redirect('index')
    else:
        signup_form = ShareeSignupForm()

    context = {
        'signup_form': signup_form,
    }
    return render(request, 'member/signup_sharee.html', context)

def signupSharer(request):
    if request.method == 'POST':
        signup_form = SharerSignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            django_login(request, user)
            return redirect('index')
    else:
        signup_form = SharerSignupForm()

    context = {
        'signup_form': signup_form,
    }
    return render(request, 'member/signup_sharer.html', context)
