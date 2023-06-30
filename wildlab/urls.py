from django.urls import path 
from wildlab import views

urlpatterns = [ 
    path('', views.Home, name='home'), 
    path('home/', views.Home, name='home'),
    path('research/', views.RESEARCH, name='research'),
    path('publication/', views.publication, name='publication'),
    path('team/', views.PEOPLE, name='team'),
    path('media/', views.MEDIA, name='media'),
    path('gallery/', views.GALLERY, name='gallery'),
    path('contact/', views.CONTACT, name='contact'),
    path('nithin/', views.nithin, name='nithin'),
    path('sreejith/', views.sreejith, name='sreejith'),
    path('joseph/', views.joseph, name='joseph'),
    path('balakrishnan/', views.balakrishnan, name='balakrishnan'),
    path('sheheer/', views.sheheer, name='sheheer'),
    path('bharati/', views.bharati, name='bharati'),
    path('ahirbudhnyan/', views.ahirbudhnyan, name='ahirbudhnyan'),
    path('ashik/', views.ashik, name='ashik'),
    path('bibin/', views.bibin, name='bibin'),
    path('deepak/', views.deepak, name='deepak'),
    path('riya/', views.riya, name='riya'),
    path('vishal/', views.vishal, name='vishal'),
    path('ajith/', views.ajith, name='ajith'),
    path('shireen/', views.shireen, name='shireen'),
    path('dinto/', views.dinto, name='dinto'),

]