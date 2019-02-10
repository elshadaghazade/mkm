from django.contrib import admin
from .models import *

admin.site.register(Regions, RegionAdmin)
admin.site.register(Schools)