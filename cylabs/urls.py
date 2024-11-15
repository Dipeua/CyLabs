from django.contrib import admin
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('', include('main.urls')),
    path('audit/', include('audit.urls')),
    path('connexion/', views.login_user, name='login'),
    path('inscription/', views.register_user, name='register'),    
    path('admin/', admin.site.urls),
]

from django.conf.urls import handler404
handler404 = 'audit.views.View404'