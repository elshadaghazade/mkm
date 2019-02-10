from django.shortcuts import render, get_object_or_404
from company_app.models import Companies
from legislation_app.models import Legislation

# Create your views here.
def legislation(request,pk):
    context = {
        'company': get_object_or_404(Companies, pk=pk),
        'company_id':pk,
    }
    context['legislations'] = Legislation.objects.filter(company_id=pk)
    return render(request, "legislation.html", context)
