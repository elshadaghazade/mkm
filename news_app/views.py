from django.shortcuts import render

# Create your views here.
def news_home(request):
    context = {}
    return render(request, "news_home.html", context)

def news_detailed(request):
    context = {}
    return render(request, "news_detailed.html", context)
    
def projects_events(request,pk):
    context = {
        'company_id':pk,
    }
    return render(request, "projects_events.html", context)

def projects_events_details(request):
    context = {}
    return render(request, "projects_events_detailed.html", context)