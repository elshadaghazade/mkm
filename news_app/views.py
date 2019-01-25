from django.shortcuts import render
from company_app.models import Companies
from news_app.models import *

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
    context['company_projects_events'] = CompanyNews.objects.filter(company_id=pk).last()
    
    return render(request, "projects_events.html", context)

def projects_events_details(request,pk):
    context = {
         'company': Companies.objects.filter(pk=pk).last(),
         'company_id': pk,
    }
    return render(request, "projects_events_detailed.html", context)