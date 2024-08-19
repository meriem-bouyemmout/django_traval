from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request, 'Home.html')

def articles_view(request):
    return render(request, 'articles.html')

def connexion_view(request):
    return render(request, 'connexion.html')

def contact_view(request):
    return render(request, 'contact.html')