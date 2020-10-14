from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Locations,Categories,Blog_Images

# Create your views here.
def welcome(request):

    allimages = Blog_Images.objects.all()

    return render(request, 'welcome.html', {"images":allimages})

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Blog_Images.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'everything/search.html',{"message":message,"imgs": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'everything/search.html',{"message":message})

def singleimage(request,image_id):
    try:
        imagez = Blog_Images.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'everything/single-picture.html', {"imagez":imagez})
