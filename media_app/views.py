from django.shortcuts import render, get_object_or_404
from company_app.models import *
from .models import *
import math
# Create your views here.
def photo_gallery(request,pk):
    company = get_object_or_404(Companies, pk=pk)
    context = {
        'company': company,
        'company_id': pk,
    }
    try:
        start = int(request.GET.get('start', 0)) - 1
    except:
        start = 0

    limit = 30
    company_count = CompanyPhotoGallery.objects.filter(company_id=company).count()

    if start < 0:
        start = 0
    elif start > math.ceil(company_count / limit):
        start = math.ceil(company_count / limit) - 1
    #TODO: make sure that this photos filtered based on company
    context['photo_list'] = CompanyPhotoGallery.objects.filter(company_id=company)[start * limit:start * limit +limit]
    context['horizontal_limit'] = 3

    return render(request, "photo_gallery.html", context)

def photo_gallery_detailed(request, pk, photo_gallery_detailed_id):
    company = get_object_or_404(Companies, pk=pk)
    context = {
        'company': company,
        'company_id': pk,
        'photos': CompanyPhotoGallery.objects.get(company=company, id=photo_gallery_detailed_id),

    }
    
    return render(request, "photo_gallery_detailed.html", context)
    
def video_gallery(request,pk):
    company = get_object_or_404(Companies, pk=pk)
    context = {
        'company': company,
        'company_id': pk,
    }
    try:
        start = int(request.GET.get('start', 0)) - 1
    except:
        start = 0

    limit = 30
    company_count = CompanyVideoGallery.objects.filter(company_id=company).count()

    if start < 0:
        start = 0
    elif start > math.ceil(company_count / limit):
        start = math.ceil(company_count / limit) - 1
    #TODO: make sure that this photos filtered based on company
    context['video_list'] = CompanyVideoGallery.objects.filter(company_id=company)[start * limit:start * limit +limit]
    context['horizontal_limit'] = 3

    return render(request, "video_gallery.html", context)

def video_gallery_detailed(request, pk, video_gallery_id):
    company = get_object_or_404(Companies, pk=pk)
    context = {
        'company': company,
        'company_id': pk,
        'videos': CompanyVideoGallery.objects.get(company=company, id=video_gallery_id),

    }
    
    return render(request, "video_gallery_detailed.html", context)