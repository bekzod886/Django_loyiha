from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import models

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


home = HomePageView()
def homeView(request):
    mevalar = models.Meva.objects.all()
    return render(request, home.template_name, {'mevalar': mevalar})
