from django.shortcuts import render
from company_app.models import Companies

# Create your views here.
def contact_main(request):
    context = {}
    return render(request, "contact_main.html", context)


def contact_company(request,pk):
    context = {
        'company':Companies.objects.get(pk=pk),
        'company_id':pk,
    }
    return render(request, "contact_company.html", context)
