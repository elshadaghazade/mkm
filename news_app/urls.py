from django.urls import path
from .views import *

urlpatterns = [
    path('', news,name='news'),
    path('<pk>/', news_detailed,name='news_detailed')
]