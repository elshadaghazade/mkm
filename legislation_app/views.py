from django.shortcuts import render
from company_app.models import Companies
from legislation_app.models import Legislation

# Create your views here.
def legislation(request,pk):
    context = {
        'company': Companies.objects.get(pk=pk),
        'company_id':pk,
    }
    context['legislations'] = Legislation.objects.filter(company_id=pk)
    return render(request, "legislation.html", context)
