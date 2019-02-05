from django.urls import path
from .views import *
from contact_app.views import contact_main
from FAQ_app.views import *

urlpatterns = [
    path('', home, name='homepage'),
    path('contacts/', contact_main, name='contact_main'),
    path('education/', education, name='education'),
    path('administration/', administration, name='administration'),
    path('documents/', documents,name='documents'),
    path('attributes/',attributes,name='attributes'),
    # path('general_information/',general_information,name="general_information"),
    path('main_faq/', main_faq,name='main_faq'),
    path('exits/',exits,name='exits'),
    path('<slug:informative_page_slug>/', informative_page, name='informative_page'),
]