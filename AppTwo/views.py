from django.shortcuts import render
from .models import Topic, Webpage, AccessRecord


# Create your views here.
def index(request):
    return render(request, 'AppTwo/home.html')

def help(request):
    return render(request, 'AppTwo/help.html')

def profile(request):
    return render(request, 'AppTwo/profile.html')

def records(request):
    topics = Topic.objects.all()
    webpages = Webpage.objects.all()
    access_records = AccessRecord.objects.all()

    context = {
        'topics': topics,
        'webpages': webpages,
        'access_records': access_records
    }

    return render(request, 'AppTwo/records.html', context)