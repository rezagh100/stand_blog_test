from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, UserEditForm
from .models import User
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated == True:
        return redirect('home:index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:index')

    else:
        form = LoginForm

    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("home:index")


def register_view(request):
    return render(request, 'account/register.html')


@login_required
def user_edit(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == 'POST':
        form = UserEditForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()

    return render(request, 'account/edit.html', {'form': form})
