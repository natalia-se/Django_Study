from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'AppTwo/home.html')

def help(request):
    return render(request, 'AppTwo/help.html')

def profile(request):
    return render(request, 'AppTwo/profile.html')