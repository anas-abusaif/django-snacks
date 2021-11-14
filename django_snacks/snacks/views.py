from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class homeView(TemplateView):
  template_name='home.html'

class aboutUsView(TemplateView):
  template_name='about_us.html'