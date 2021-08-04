from django.urls import path
from .views import HomePageView, homeView
from loyihaapp import views

urlpatterns = [
    path('', homeView, name='index'),
    path('about/', views.aboutView, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login/praktika/',views.praktika, name='praktika'),
]
