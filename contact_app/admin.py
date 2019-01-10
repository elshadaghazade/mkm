from django.contrib import admin
from .models import ContactCompany, \
    ContactCompanyForm, \
    ContactCompanyReceivedEmails, \
    ContactMainForm, \
    ContactMainReceivedEmails


# Register your models here.
admin.site.register(ContactCompany)
admin.site.register(ContactCompanyForm)
admin.site.register(ContactCompanyReceivedEmails)
admin.site.register(ContactMainForm)
admin.site.register(ContactMainReceivedEmails)
