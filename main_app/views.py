from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}

    return render(request, "home.html", context)

def education(request):
    context = {}
    return render(request, "education.html", context)
    
def administration(request):
    context = {}
    return render(request, "administration_main.html", context)

def media(request):
    context = {}
    return render(request, "media.html", context)