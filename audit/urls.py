from django.urls import path
from audit import views

from accounts.views import logout_user

urlpatterns = [
    path('', views.index, name='audit'),
    path('scanning/', views.scanning, name='scanning'),
    path('repport/', views.repport, name='repport'),
    path('informations/', views.informations, name='informations'),
    path('ports/', views.ports, name='ports'),
    path('vulnerabiliter/', views.vulnerability, name='vulnerability'),
    path('deconnecter/', logout_user, name='logout'),
]
