from django.shortcuts import render
from company_app.models import Companies
from news_app.models import *
from django.db.models import Count
import math

# Create your views here.
def news_home(request):
    context = {}
    return render(request, "news_home.html", context)

def news_detailed(request):
    context = {}
    return render(request, "news_detailed.html", context)
    
def projects_events(request,pk):
    context = {
        'company': Companies.objects.filter(pk=pk).last(),
        'company_id': pk,
    }

    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    

    limit = 10
    cnt = CompanyNews.objects.filter(company_id=pk).aggregate(Count("id"))['id__count']
    cnt = math.ceil(cnt / limit)

    if page < 1:
        page = 1
    elif page > cnt:
        page = cnt

    start = (page - 1) * limit
    end = start + limit

    prev_btn = next_btn = 0

    if page - 1 < 1:
        prev_btn = 1
    else:
        prev_btn = page - 1

    if page + 1 > cnt:
        next_btn = cnt
    else:
        next_btn = page + 1


    context['company_projects_events'] = CompanyNews.objects.filter(company_id=pk).order_by('-publish_date')[start:end]
    context['total_pages'] = range(1, cnt+1)
    context['selected_page'] = page
    context['start_btn'] = 1
    context['end_btn'] = cnt
    context['prev_btn'] = prev_btn
    context['next_btn'] = next_btn
    context['total_pages_int'] = cnt
    
    return render(request, "projects_events.html", context)

def projects_events_details(request,pk,news_id):
    company = Companies.objects.get(pk=pk)
    context = {
         'company': Companies.objects.filter(pk=pk),
         'company_id': pk,
         'news_id':CompanyNews.objects.filter(company_id=company,id=news_id ),
    }
    return render(request, "projects_events_details.html", context)