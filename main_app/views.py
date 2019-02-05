from django.shortcuts import render
from main_app.models import *


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

def documents(request):
    context = {}
    context['document_files'] = Documents.objects.all()
    return render(request,"documents.html",context)

def attributes(request):
    context={}
    context['attributes'] = Attributes.objects.all()
    return render(request,'attributes.html',context)

def informative_page (request, informative_page_slug):

    try:
        page = MainInformativePages.objects.get(slug=informative_page_slug)
    except:
        context = {
            'page_title': '',
            'page_slug': '',
            'page_full_content': '',
            'page_short_description': ''
        }
    else:
        context = {
            'page_title': page.title,
            'page_slug': page.slug,
            'page_full_content': page.full_content,
            'page_short_description': page.short_description
        }

    print(context)
    
    # context['information'] = GeneralInformation.objects.all().last()
    return render(request,"informative_page.html", context)

def exits(request):
    context={}
    context['exits'] = Exits.objects.all()
    return render(request,'exits.html',context)