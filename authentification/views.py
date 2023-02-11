from django.shortcuts import render, HttpResponse, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signin(request):
    if request.method == 'POST':
        userform = AuthenticationForm(data=request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('news')
    else:
        userform = AuthenticationForm()
        return render(request, template_name='authentification/signin.html', context={'form': userform})


def signup(request):
    if request.method == 'POST':
        userform = CreateUserForm(request.POST)
        if userform.is_valid():
            userform.save()
            username = userform.cleaned_data['password1']
            messages.success(request, f'Account created succesfully for {username}')
            return redirect('signin')
        else:
            return render(request, template_name='authentification/signup.html', context={'form': userform})
    else:
        userform = CreateUserForm()
        return render(request, template_name='authentification/signup.html', context={'form': userform})
