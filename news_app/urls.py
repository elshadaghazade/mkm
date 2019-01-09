from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='name_id'),
    path('<pk>/', news_detailed,name='news_detailed')
]