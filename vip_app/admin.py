from django.contrib import admin
from vip_app.models import *

# Register your models here.

class VipDescStackInline(admin.StackedInline):
    model = VipDescription
    extra = 3

@admin.register(VIP)
class VIPAdmin(admin.ModelAdmin):
    inlines = [VipDescStackInline]

