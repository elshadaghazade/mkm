from django.shortcuts import render

# Create your views here.
def news(request):
    context = {}
    return render(request, "news.html", context)

def news_detailed(request):
    context = {}
    return render(request, "news_detailed.html", context)
    
def projects_events(request):
    context = {}
    return render(request, "projects_events.html", context)

def projects_events_details(request):
    context = {}
    return render(request, "projects_events_detailed.html", context)