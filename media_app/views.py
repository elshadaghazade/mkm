from django.shortcuts import render
from company_app.models import *
import math
# Create your views here.
def photo_gallery(request,pk):
    context = {
        'company': Companies.objects.get(pk=pk),
        'company_id': pk,
    }
    
    try:
        start = int(request.GET.get('start', 0)) - 1
    except:
        start = 0

    limit = 100
    company_count = CompanyPhotoGallery.objects.count()

    if start < 0:
        start = 0
    elif start > math.ceil(company_count / limit):
        start = math.ceil(company_count / limit) - 1

    context['photo_list'] = CompanyPhotoGallery.objects.all()[start * limit:start * limit +limit]
    context['horizontal_limit'] = 3

    return render(request, "photo_gallery.html", context)

def photo_gallery_detailed(request,pk,photo_gallery_id):
    context = {
        'company': Companies.objects.get(pk=pk),
        'company_id': pk,
        #'photo_id': photo_gallery_id,
    }
    
    return render(request, "photo_gallery_detailed.html", context)
    
def video_gallery(request):
    context = {}
    return render(request, "video_gallery.html", context)

def video_gallery_detailed(request):
    context = {}
    return render(request, "video_gallery_detailed.html", context)