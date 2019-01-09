from django.shortcuts import render

# Create your views here.
def legislation(request):
    context = {}
    return render(request, "legislation.html", context)
