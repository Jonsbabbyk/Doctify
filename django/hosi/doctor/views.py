from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

def index(request):
    # Add your view logic here
    return render(request, 'index.html')


class HomeTemplateView(TemplateView):
    template_name ="index.html"