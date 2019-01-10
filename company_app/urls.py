from django.urls import path
from company_app.views import *
from vip_app.views import *
from news_app.views import *
from legislation_app.views import legislation
from FAQ_app.views import faq
from media_app.views import *
from contact_app.views import contact_company

urlpatterns = [
    path('', companies, name='companies'),
    path('<pk>/', company,name='company'),
    path('<pk>/about/', about, name='about'),
    path('<pk>/administration/', administration,name='administration'),
    path('<pk>/achievements/', achievements,name='achievements'),
    path('<pk>/medalists/', medalist,name='medalist'),
    path('<pk>/distinquished/', distinguished_ones,name='distinguished_ones'),
    path('<pk>/projects-and-events/', projects_events,name='projects_events'),
    path('<pk>/projects-and-events/<int:news_id>/', projects_events_details,name='projects_events_details'),
    path('<pk>/legislation/', legislation,name='legislation'),
    path('<pk>/admission/', admission,name='admission'),
    path('<pk>/faq/', faq,name='faq'),
    path('<pk>/photos/', photo_gallery,name='photo_galleries'),
    path('<pk>/photos/<int:photo_gallery_id>/', photo_gallery,name='photo_gallery'),
    path('<pk>/videos/', video_gallery,name='video_gallery'),
    path('<pk>/videos/<int:video_gallery_id>/', video_gallery_detailed,name='video_gallery_detailed'),
    path('<pk>/contacts/', contact_company,name='contact_company')
]
