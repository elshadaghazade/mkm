from django.shortcuts import render
from company_app.models import Companies
from FAQ_app.models import *

# Create your views here.
def faq(request,pk):
    context = {
        'company': Companies.objects.get(pk=pk),
        'company_id': pk,
    }
    context['faqs'] = Faq.objects.filter(company_id=pk)
    return render(request, "faq.html", context)

def main_faq(request):
    context = {}
    context['main_faqs'] = MainFaq.objects.all()
    return render(request,'main_faq.html',context)