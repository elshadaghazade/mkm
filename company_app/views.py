from django.shortcuts import render
from company_app.models import Companies


class Counter:
    count = 1

    def increment(self):
        self.count += 1
        return ''

    def set_to_one(self):
        self.count = 1
        return ''


# Create your views here.
def companies(request):
    context = {}
    #cp_id = Companies.objects.get(pk=pk)
    context['company_list'] = Companies.objects.all()
    context['counter'] = Counter()
    return render(request, "companies.html", context)


def company(request, pk):
    context = {}
    return render(request, 'company.html', context)


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


def distinquished(request):
    """
    The view for excellent guys who are in hall of the fame
    :param request:
    :return:
    """
    context = {}
    return render(request, "distinquished.html", context)
