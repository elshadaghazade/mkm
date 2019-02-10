from django.contrib import admin
from company_app.models import *

admin.site.register(Companies, CompaniesAdmin)
# admin.site.register(CompanyAdministration, CompanyAdministrationAdmin)
admin.site.register(CompanyInformativePages, CompanyInformativePagesAdmin)
