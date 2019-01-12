from django.contrib import admin
from news_app.models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(NewsCategories)
admin.site.register(News)
admin.site.register(CompanyNews)
