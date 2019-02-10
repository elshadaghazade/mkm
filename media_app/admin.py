from django.contrib import admin
from .models import *

admin.site.register(CompanyPhotoGallery, CompanyPhotoGalleryAdmin)
admin.site.register(CompanyVideoGallery, CompanyVideoGalleryAdmin)
