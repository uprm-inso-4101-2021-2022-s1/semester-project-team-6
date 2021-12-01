from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def bootstrap(request):
    return render(request, 'bootstrap.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')