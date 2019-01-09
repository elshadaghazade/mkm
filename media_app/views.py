from django.shortcuts import render

# Create your views here.
def photo_gallery(request):
    context = {}
    return render(request, "photo_gallerry.html", context)

def photo_gallery_detailed(request):
    context = {}
    return render(request, "photo_gallery_detailed.html", context)
    
def video_gallery(request):
    context = {}
    return render(request, "video_gallery.html", context)

def video_gallery_detailed(request):
    context = {}
    return render(request, "video_gallery_detailed.html", context)