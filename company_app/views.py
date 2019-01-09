from django.shortcuts import render

# Create your views here.
def company(request):
    context = {}
    return render(request, "company", context)

def about(request):
    context = {}
    return render(request, "about.html", context)

def administration(request):
    context = {}
    return render(request, "administration_company.html", context)

def achievements(request):
    context = {}
    return render(request, "achievements.html", context)

def admission(request):
    context = {}
    return render(request, "admission.html", context)