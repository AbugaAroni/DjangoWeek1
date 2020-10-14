from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):

    images = Images.objects.all()

    return render(request, 'welcome.html', {"images":images})
