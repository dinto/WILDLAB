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

]