from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from company_app.models import Companies
from vip_app.models import VIP
from legislation_app.models import Legislation
from news_app.models import CompanyNews
from FAQ_app.models import Faq
from media_app.models import CompanyPhotoGallery, CompanyVideoGallery
from contact_app.models import ContactCompany
from django.db.models import Q

@csrf_exempt
def search_inside_company(request):

    data = []
    
    try:
        cid = int(request.POST.get('cid', -1))
        v = request.POST.get('v', '')
        if Companies.objects.filter(pk=cid, about__icontains=v).count() > 0:
            data.append('about')

        if Companies.objects.filter(pk=cid, administration__icontains=v).count() > 0:
            data.append('administration')

        if Companies.objects.filter(pk=cid, achievements__icontains=v).count() > 0:
            data.append('achievements')

        if Companies.objects.filter(pk=cid, admission_requirements__icontains=v).count() > 0:
            data.append('admission')

        if VIP.objects.filter(Q(full_name__icontains=v) | Q(short_description__icontains=v), company=Companies.objects.get(pk=cid), vip_type=VIP.VIP_MEDAL_ALANLAR).count() > 0:
            data.append('medalists')

        if VIP.objects.filter(Q(full_name__icontains=v) | Q(short_description__icontains=v), company=Companies.objects.get(pk=cid), vip_type=VIP.VIP_FERQLENENLER).count() > 0:
            data.append('distinguished')


        if Legislation.objects.filter(company=Companies.objects.get(pk=cid), title__icontains=v).count() > 0:
            data.append('legislation')

        if CompanyNews.objects.filter(Q(title__icontains=v) | Q(short_description__icontains=v) | Q(text__icontains=v), company=Companies.objects.get(pk=cid)).count() > 0:
            data.append('projects_events')

        if Faq.objects.filter(Q(question__icontains=v) | Q(answer__icontains=v), company=Companies.objects.get(pk=cid)).count() > 0:
            data.append('faq')

        if CompanyPhotoGallery.objects.filter(Q(title__icontains=v) | Q(content__icontains=v), company=Companies.objects.get(pk=cid)).count() > 0:
            data.append('photo_galleries')

        if CompanyVideoGallery.objects.filter(Q(title__icontains=v) | Q(content__icontains=v), company=Companies.objects.get(pk=cid)).count() > 0:
            data.append('video_galleries')

        if ContactCompany.objects.filter(contact__icontains=v, company=Companies.objects.get(pk=cid)).count() > 0:
            data.append('contacts')

        
    except Exception as err:
        return JsonResponse({
            'status': 'ERROR',
            'error_msg': 'company was not found' + str(err),
            'data': []
        })
    else:
        return JsonResponse({
            'status': 'OK',
            'error_msg': None,
            'data': data
        })