from django.shortcuts import render
from django.http import HttpResponse
from .models import Locations,Categories,Blog_Images

# Create your views here.
def welcome(request):

    allimages = Blog_Images.objects.all()

    return render(request, 'welcome.html', {"images":allimages})
