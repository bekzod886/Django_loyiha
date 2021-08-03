from django.urls import path
from .views import HomePageView, homeView

urlpatterns = [
    path('', homeView, name='index')
]
