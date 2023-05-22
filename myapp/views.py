from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.

def index(request):
    feature1 = Feature()
    feature1.name = 'Balkrishna'
    feature1.id = 1
    feature1.details = 'hello world'
  
    return render (request, 'index.html',{'feature':feature1})
