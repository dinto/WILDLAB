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
    path('Wildlife_human_dynamics/', views.research1, name='research1'),
    path('Biology_conservation_threatened_species/', views.research2, name='research2'),
    path('Surveys_and_population_assessment/', views.research3, name='research3'),
    path('Wildlife_ecology_behavioural_ecology_and_community_ecology/', views.research4, name='research4'),
    path('Life_history_evolution_and_natural_history/', views.research5, name='research5'),
    path('Citizen_Science_Outreach_Stakeholder_Engagement/', views.research6, name='research6'),
    
    path('Sreehari_Raman/', views.Sreehari_Raman, name='Sreehari_Raman'),

]