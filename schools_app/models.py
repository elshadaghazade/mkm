from django.db import models
from django import forms
from django.contrib import admin

class Regions(models.Model):
    region_id = models.IntegerField('Region ID')
    name = models.CharField('Regionun adı', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regionlar'

class Schools(models.Model):
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    school_id = models.IntegerField('Məktəb İD')
    name = models.CharField('Məktəbin adı', max_length=255)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} - {self.region}"

    class Meta:
        verbose_name = "Məktəb"
        verbose_name_plural = "Mətkəblər"


######### admin ###############
class RegionForm(forms.ModelForm):
    model = Regions

    class Meta:
        widgets = {
            'region_id': forms.NumberInput(attrs={'placeholder': 'region id', 'readonly': True}),
        }

    class Media:
        js = ('//ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js', 'js/region_admin_validate.js')

class RegionAdmin(admin.ModelAdmin):
    form = RegionForm