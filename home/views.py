from django.contrib.auth.models import User
from . import forms
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'text.html')

def register(request):
    if(request.method == 'POST'):
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home/')
    
    else:
        form = forms.RegistrationForm()
    args = {'form': form}
    return render(request, 'register.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = forms.EditProfile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('')

    else:
        form = forms.EditProfile(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)