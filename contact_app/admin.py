from django.contrib import admin
from .models import *

admin.site.register(ContactCompany, ContactCompanyAdmin)
admin.site.register(ContactCompanyForm, ContactCompanyFormAdmin)
admin.site.register(ContactCompanyReceivedEmails)
admin.site.register(ContactMainForm)
admin.site.register(ContactMainReceivedEmails)
