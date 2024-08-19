
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('articles/', views.articles_view, name='articles'),
    path('connexion/', views.connexion_view, name='connexion'),
    path('contact/', views.contact_view, name='contact'),
]
