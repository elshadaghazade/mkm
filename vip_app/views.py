from django.shortcuts import render
from company_app.models import Companies
from vip_app.models import *


# Create your views here.

def medalist(request,pk):
    context = {
        'company': Companies.objects.filter(pk=pk).last(),
        'company_id': pk,
    }
    context['medalist'] = VIP.objects.filter(
        company_id=pk,
        vip_type=VIP.VIP_MEDAL_ALANLAR,
    )
    return render(request, "medalist.html", context)


def distinguished_ones(request,pk):
    context = {
        'company': Companies.objects.filter(pk=pk).last(),
        'company_id': pk,
    }
    context['distinguished_ones'] = VIP.objects.filter(
        company_id=pk,
        vip_type=VIP.VIP_FERQLENENLER,
        )

    
    return render(request, "distinguished_ones.html", context)



