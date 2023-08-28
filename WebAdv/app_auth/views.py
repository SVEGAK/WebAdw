from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm

def register_view(request): 
    if request.method == "POST": 
        form = ExtendedUserCreationForm(request.POST, request.FILES)
        if form.is_valid(): 
            new_user = form.save(commit=False)
            new_user.user = request.user
            new_user.save()
            url = reverse('login')
            return redirect(url)
 
    else: 
        form = ExtendedUserCreationForm() 
    context = {'form':form} 
    return render(request, 'app_auth/register.html', context)
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')
def login_view(request):
    profile_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(profile_url)
        else:
            return render(request, 'app_auth/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(profile_url)
        else:
            return render(request, 'app_auth/login.html', {"error": 'Пользователь не найден. Проверьте правильность заполнения полей.'})
        