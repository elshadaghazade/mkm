from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(ContactCompany, ContactCompanyAdmin)
admin.site.register(ContactCompanyForm, ContactCompanyFormAdmin)
admin.site.register(ContactCompanyReceivedEmails)
admin.site.register(ContactMainForm)
admin.site.register(ContactMainReceivedEmails)
