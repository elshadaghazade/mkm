from django.shortcuts import render

# Create your views here.
def contact_main(request):
    context = {}
    return render(request, "contact_main.html", context)

def contact_company(request):
    context = {}
    return render(request, "contact_company.html", context)