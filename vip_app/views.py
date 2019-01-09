from django.shortcuts import render

# Create your views here.
def distinguished_ones(request):
    context = {}
    return render(request, "distinguished_ones.html", context)

def medalist(request):
    context = {}
    return render(request, "medalist.html", context)
