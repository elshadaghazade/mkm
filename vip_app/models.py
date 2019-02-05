from django.db import models
from company_app.models import Companies
from django.contrib import admin


# Create your models here.
class VIP(models.Model):
    VIP_MEDAL_ALANLAR = 1
    VIP_FERQLENENLER = 2

    VIP_TYPE_CHOICES = (
        (VIP_MEDAL_ALANLAR, 'Medal alanlar'),
        (VIP_FERQLENENLER, 'Fərqlənənlər')
    )

    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    vip_type = models.IntegerField("Kateqoriya", choices=VIP_TYPE_CHOICES)
    full_name = models.CharField("Ad və Soyad", max_length=255)
    short_description = models.TextField("Qısa təsvir", max_length=255)
    image = models.ImageField("Şəkil", upload_to='media')

    def __str__(self):
        return f"{self.full_name} ({list(filter(lambda x: x[0] == self.vip_type, self.VIP_TYPE_CHOICES))[0][1]})"

    class Meta:
        verbose_name = "Fərqlənənlər və Medal alanlar"
        verbose_name_plural = "Fərqlənənlər və Medal alanlar"


##### VIP ADMIN #######
class VIPAdmin(admin.ModelAdmin):
    exclude = "company",

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.company = Companies.objects.get(profile=request.user)

        super(VIPAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(VIPAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(company=Companies.objects.get(profile=request.user))


