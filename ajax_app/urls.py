from django.urls import path
from .views import *

urlpatterns = [
    path('search_inside_company/', search_inside_company)
]
