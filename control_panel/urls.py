from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name="cpanel_home_page"),
    path('login/', LoginView.as_view(), name="cpanel_login_page")
]
