from django.urls import path
from . import views

urlpatterns = [
    path('tableau/', views.tableau_de_bord, name='tableau'),
    path('conducteurs/', views.conducteur_list, name='conducteur_list'),
    path('conducteurs/search/', views.conducteur_search, name='conducteur_search'),
    path('conducteurs/edit/<int:pk>/', views.conducteur_edit, name='conducteur_edit'),    
    # path('', views.accueil, name='accueil'),
    # path('a-propos/', views.about, name='apropos'),
    # path('services/', views.services, name='services'),
    # path('contact/', views.contact, name='contact'),

]
