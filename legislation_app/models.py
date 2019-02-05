from django.db import models
from company_app.models import Companies
from django.contrib import admin

class Legislation(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    title = models.CharField("Başlıq", max_length=255)
    legislation_file = models.FileField(verbose_name="Yükləmə", upload_to="media")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Qanunvericilik"
        verbose_name_plural = "Qanunvericilik"


##### Legislation ADMIN #######
class LegislationAdmin(admin.ModelAdmin):
    exclude = "company",

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.company = Companies.objects.get(profile=request.user)

        super(LegislationAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(LegislationAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(company=Companies.objects.get(profile=request.user))