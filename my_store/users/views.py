from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/Login.html', context)



def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
<<<<<<< HEAD
            messages.success(request, 'Поздравляем! Вы успешно зарегистрирвоались!')
=======
>>>>>>> dcdc65fdec92ea8fe2390f19f0d9f238fae3e9ca
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm
    context = {'form': form}
    return render(request, "users/registration.html", context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'Store - Профиль', 'form': form}
    return render(request, 'users/profile.html', context)
