from django.shortcuts import render
from wildlab.models import News_Update

# Create your views here.
def Home(request): 
    news=News_Update.objects.all()
    return render(request,'index.html',{"news":news})

def RESEARCH(request): 
    return render(request,'research.html',{})

def PEOPLE(request): 
    return render(request,'PEOPLE.html',{})
def publication(request): 
    return render(request,'publication.html',{})
def MEDIA(request): 
    return render(request,'MEDIA.html',{})
def GALLERY(request): 
    return render(request,'GALLERY.html',{})
def CONTACT(request): 
    return render(request,'CONTACT.html',{})

