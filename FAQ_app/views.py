from django.shortcuts import render

# Create your views here.
def faq(request):
    context = {}
    return render(request, "faq.html", context)