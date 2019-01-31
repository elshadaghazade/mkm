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

def general_information(request):
    context = {}
    context['information'] = GeneralInformation.objects.all().last()
    return render(request,"General_information.html",context)

def exits(request):
    context={}
    context['exits'] = Exits.objects.all()
    return render(request,'exits.html',context)