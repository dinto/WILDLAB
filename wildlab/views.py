from django.shortcuts import render
from wildlab.models import News_Update,Publication

# Create your views here.
def Home(request): 
    news=News_Update.objects.all()
    return render(request,'index.html',{"news":news})

def RESEARCH(request): 
    return render(request,'research.html',{})

def PEOPLE(request): 
    return render(request,'PEOPLE.html',{})
def publication(request): 
    Publications=Publication.objects.all().order_by('-id')
    return render(request,'publication.html',{"Publications":Publications})
def MEDIA(request): 
    return render(request,'MEDIA.html',{})
def GALLERY(request): 
    return render(request,'GALLERY.html',{})
def CONTACT(request): 
    return render(request,'CONTACT.html',{})
def nithin(request): 
    return render(request,'nithin.html',{})
def sreejith(request): 
    return render(request,'sreejith.html',{})

def joseph(request): 
    return render(request,'joseph.html',{})
def balakrishnan(request): 
    return render(request,'balakrishnan.html',{})
def sheheer(request): 
    return render(request,'sheheer.html',{})
def bharati(request): 
    return render(request,'bharati.html',{})
def ahirbudhnyan(request): 
    return render(request,'ahirbudhnyan.html',{})
def ashik(request): 
    return render(request,'ashik.html',{})
def bibin(request): 
    return render(request,'bibin.html',{})
def deepak(request): 
    return render(request,'deepak.html',{})
def riya(request): 
    return render(request,'riya.html',{})
def vishal(request): 
    return render(request,'vishal.html',{})
def ajith(request): 
    return render(request,'ajith.html',{})
def shireen(request): 
    return render(request,'shireen.html',{})
def dinto(request): 
    return render(request,'dinto.html',{})
def research1(request): 
    return render(request,'research1.html',{})
def research2(request): 
    return render(request,'research2.html',{})
def research3(request): 
    return render(request,'research3.html',{})
def research4(request): 
    return render(request,'research4.html',{})
def research5(request): 
    return render(request,'research5.html',{})
def research6(request): 
    return render(request,'research6.html',{})
    