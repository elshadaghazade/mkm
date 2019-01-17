from django.shortcuts import render
from company_app.models import Companies

# Create your views here.
def legislation(request,pk):
    context = {
        'company': Companies.objects.get(pk=pk),
        'company_id':pk,
    }
    return render(request, "legislation.html", context)
