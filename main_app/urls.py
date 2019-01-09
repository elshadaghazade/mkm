from django.urls import path
from .view import *
from contact_app.views import contact_main

urlpatterns = [
    path('', home,name='home'),
    path('contactus/', contact_main,name='contact_main'),
    path('education/', education,name='education'),
    path('administration/', administration,name='administration'),
]