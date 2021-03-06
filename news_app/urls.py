from django.urls import path
from .views import *

urlpatterns = [
    path('news/', news,name='news'),
    path('news/<pk>/', news_detailed,name='news_detailed'),
    path('events/', events,name='events'),
    path('events/<pk>/', events_detailed,name='events_detailed'),
    path('speeches/', speeches,name='speeches'),
    path('speeches/<pk>/', speeches_detailed,name='speeches_detailed')
]