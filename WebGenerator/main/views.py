from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django import forms
from .forms import GeneratorForm
from .models import Form
from django.urls import reverse_lazy, reverse


def index(request):
    return render(request, 'main/index.html')


def prising(request):
    return render(request, 'main/prising.html')


#def generator(request):
    #return render(request, 'main/generator.html')


def generator(request):
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        location = request.POST.get('location')
        number = request.POST.get('number')

        lead = Form(keywords=keywords, location=location, number=number)
        lead.save()
        return redirect('success')


    form = GeneratorForm()
    content = {
        'form': form,
        }

    return render(request, 'main/generator.html', content)


def login(request):
    return render(request, 'main/login1.html')


def signup(request):
    return render(request, 'main/signup.html')


def success(request):
    return render(request, 'main/success.html')

def FAQs (request):
    return render(request, 'main/FAQs.html')


def aboutus (request):
    return render(request, 'main/aboutus.html')


def contacts (request):
    return render(request, 'main/contacts.html')



#1

