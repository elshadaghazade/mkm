from django.shortcuts import render, get_list_or_404, get_object_or_404
from company_app.models import Companies
from news_app.models import *
from django.db.models import Count, Q
from django.core.paginator import Paginator
import math

# Create your views here.
def news(request):
    context = {}

    context['news'] = News.objects.all().order_by('-publish_date')[start:end]
    return render(request, "news.html", context)

def news_detailed(request):
    context = {}
    return render(request, "news_detailed.html", context)
    
def projects_events(request,pk):
    company = get_object_or_404(Companies, pk=pk)
    context = {
        'company': company,
    }


    company_news = CompanyNews.objects.filter(company=company).order_by('-publish_date')
    context['paginator'] = Paginator(company_news, 2)
    context['news'] = context['paginator'].get_page(request.GET.get('page', 1))
    
    return render(request, "projects_events.html", context)

def projects_events_details(request,pk,news_id):

    company = get_object_or_404(Companies, pk=pk)
    news = CompanyNews.objects.filter(pk=news_id, company=company).order_by('companynewsslideimages__weight')[0]
    related_news = []
    
    for rnews in CompanyNews.objects.filter(~Q(id=news.id) & Q(category=news.category))[:2]:
        rnews.news_date = rnews.publish_date.strftime("%A, %d %B %Y")
        rnews.news_time = rnews.publish_date.strftime("%H:%M")
        related_news.append(rnews)



    context = {
         'company': company,
         'news': news,
         'news_date': news.publish_date.strftime("%A, %d %B %Y"),
         'news_time': news.publish_date.strftime("%H:%M"),
         'related_news': related_news
    }
    
    return render(request, "projects_events_details.html", context)