from django.shortcuts import render
from company_app.models import Companies
import math


# Create your views here.
def companies(request):
    try:
        start = int(request.GET.get('start', 0)) - 1
    except:
        start = 0

    context = {}
    limit = 3
    company_count = Companies.objects.count()

    if start < 0:
        start = 0
    elif start > math.ceil(company_count / limit):
        start = math.ceil(company_count / limit) - 1

    context['selected_page'] = start + 1
    context['company_list'] = Companies.objects.all()[start * limit:start * limit +limit]
    pages_count = math.ceil(company_count / limit)
    context['total_pages'] = range(1, pages_count+1)
    context['horizontal_limit'] = 3
    context['next_page'] = start + 2 if start + 2 < pages_count else pages_count
    context['prev_page'] = start if start > 0 else 1

    return render(request, "companies.html", context)


def company(request, pk):
    context = {
        'company': Companies.objects.get(pk=pk),
        'company_id': pk,
    }

    return render(request, 'company.html', context)


def about(request, pk):
    context = {
        'company': Companies.objects.get(pk=pk),
        'company_id': pk,

    }
    comps = Companies.objects.all()
    context['comps'] = comps 
    return render(request, "about.html", context)


def administration(request,pk):
    context = {
        'company': Companies.objects.get(pk=pk),
        'company_id': pk,
    }
    return render(request, "administration_company.html", context)


def achievements(request,pk):
    context = {
        'company': Companies.objects.get(pk=pk),
        'company_id': pk,
    }
    return render(request, "achievements.html", context)


def admission(request,pk):
    context = {
        'company':Companies.objects.get(pk=pk),
        'company_id':pk,
    }
    return render(request, "admission.html", context)


def distinquished(request):
    """
    The view for excellent guys who are in hall of the fame
    :param request:
    :return:
    """
    context = {}
    return render(request, "distinquished.html", context)
