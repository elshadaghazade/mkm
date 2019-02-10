from django.shortcuts import render, get_list_or_404, get_object_or_404
from company_app.models import Companies
from news_app.models import *
from django.db.models import Count, Q
from django.core.paginator import Paginator
import math

# Create your views here.
def news(request):
    context = {}
    company_news = News.objects.filter(type=News.TYPE_NEWS).order_by('-publish_date')
    context['paginator'] = Paginator(company_news, 2)
    context['news'] = context['paginator'].get_page(request.GET.get('page', 1))
    
    return render(request, "news.html", context)

def news_detailed(request, pk):
    news = get_list_or_404(News.objects.filter(pk=pk, type=News.TYPE_NEWS).order_by('newsslideimages__weight'))[0]
    related_news = []
    
    for rnews in News.objects.filter(~Q(id=news.id) & Q(category=news.category) & Q(type=News.TYPE_NEWS))[:2]:
        rnews.news_date = rnews.publish_date.strftime("%A, %d %B %Y")
        rnews.news_time = rnews.publish_date.strftime("%H:%M")
        related_news.append(rnews)



    context = {
         'news': news,
         'news_date': news.publish_date.strftime("%A, %d %B %Y"),
         'news_time': news.publish_date.strftime("%H:%M"),
         'related_news': related_news
    }
    
    return render(request, "news_detailed.html", context)

def events(request):
    context = {}
    company_events = News.objects.filter(type=News.TYPE_EVENT).order_by('-publish_date')
    context['paginator'] = Paginator(company_events, 2)
    context['events'] = context['paginator'].get_page(request.GET.get('page', 1))
    
    return render(request, "events.html", context)

def events_detailed(request, pk):
    events = get_list_or_404(News.objects.filter(pk=pk, type=News.TYPE_EVENT).order_by('newsslideimages__weight'))[0]
    related_events = []
    
    for rnews in News.objects.filter(~Q(id=events.id) & Q(category=events.category) & Q(type=News.TYPE_EVENT))[:2]:
        rnews.event_date = rnews.publish_date.strftime("%A, %d %B %Y")
        rnews.event_time = rnews.publish_date.strftime("%H:%M")
        related_events.append(rnews)



    context = {
         'events': events,
         'event_date': events.publish_date.strftime("%A, %d %B %Y"),
         'event_time': events.publish_date.strftime("%H:%M"),
         'related_events': related_events
    }
    
    return render(request, "events_detailed.html", context)

def speeches(request):
    context = {}
    company_speeches = News.objects.filter(type=News.TYPE_SPEECH).order_by('-publish_date')
    context['paginator'] = Paginator(company_speeches, 2)
    context['speeches'] = context['paginator'].get_page(request.GET.get('page', 1))
    
    return render(request, "speeches.html", context)

def speeches_detailed(request, pk):
    events = News.objects.filter(pk=pk, type=News.TYPE_SPEECH).order_by('newsslideimages__weight')[0]
    related_speeches = []
    
    for rnews in News.objects.filter(~Q(id=events.id) & Q(category=events.category) & Q(type=News.TYPE_SPEECH))[:2]:
        rnews.event_date = rnews.publish_date.strftime("%A, %d %B %Y")
        rnews.event_time = rnews.publish_date.strftime("%H:%M")
        related_speeches.append(rnews)



    context = {
         'speeches': events,
         'speech_date': events.publish_date.strftime("%A, %d %B %Y"),
         'speech_time': events.publish_date.strftime("%H:%M"),
         'related_speeches': related_speeches
    }
    
    return render(request, "speeches_detailed.html", context)
    
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