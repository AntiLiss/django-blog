from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import forms


# Create your views here.
def signin(request):
    return render(request, template_name='authentification/signin.html', context={'form': forms.UserForm})


def signup(request):
    if request.method == 'POST':
        userform = forms.UserForm(request.POST)
        if userform.is_valid():
            # userform.save()
            return render(request, template_name='main/news.html')
        else:
            return HttpResponse('Invalid data')
    else:
        return render(request, template_name='authentification/signup.html', context={'form': forms.UserForm})