from django.shortcuts import render
from company_app.models import Companies


# Create your views here.
def distinguished_ones(request,pk):
    context = {
        'company': Companies.objects.get(pk=pk),
        'company_id': pk,
    }
    return render(request, "distinguished_ones.html", context)


def medalist(request,pk):
    context = {
        'company': Companies.objects.get(pk=pk),
        'company_id': pk,
    }
    return render(request, "medalist.html", context)
