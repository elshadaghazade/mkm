from django.contrib import admin
from FAQ_app.models import * 
# Register your models here.

admin.site.register(Faq, FAQAdmin)
admin.site.register(MainFaq)