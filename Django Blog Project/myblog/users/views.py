from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #saving the user into the db
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('users-login')

    context = {
        'form':form
    }
    return render(request, 'users/register.html', context)


def logout(request):
    logout_user(request)
    messages.success(request, 'You have logged out!')
    return redirect('users-login')


@login_required
def profile(request):
    return render(request, 'users/profile.html')