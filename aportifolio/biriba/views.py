from django.shortcuts import render

from .import views

def IndexView(request):
    return render(request, 'biriba/index.html')
