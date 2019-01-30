from django.urls import path
from .views import *
from contact_app.views import contact_main

urlpatterns = [
    path('', home, name='homepage'),
    path('contacts/', contact_main, name='contact_main'),
    path('education/', education, name='education'),
    path('administration/', administration, name='administration'),
    path('documents/', documents,name='documents')
]