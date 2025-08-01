from django.urls import path
from . import views

urlpatterns = [
    path('tableau/', views.tableau_de_bord, name='tableau'),
    # path('', views.accueil, name='accueil'),
    # path('a-propos/', views.about, name='apropos'),
    # path('services/', views.services, name='services'),
    # path('contact/', views.contact, name='contact'),

]
