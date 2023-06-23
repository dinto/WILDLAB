from django.urls import path 
from wildlab import views

urlpatterns = [ 
    path('', views.Home, name='home'), 
    path('home/', views.Home, name='home'),
    path('RESEARCH/', views.RESEARCH, name='RESEARCH'),
    path('publication/', views.publication, name='publication'),
    path('PEOPLE/', views.PEOPLE, name='PEOPLE'),
    path('MEDIA/', views.MEDIA, name='MEDIA'),
    path('GALLERY/', views.GALLERY, name='GALLERY'),
    path('CONTACT/', views.CONTACT, name='CONTACT'),

]