from django.contrib import admin
from news_app.models import *
from company_app.models import Companies

admin.site.register(Category, CategoryAdmin)
# admin.site.register(NewsCategories)
admin.site.register(News)
admin.site.register(CompanyNews, CompanyNewsAdmin)
