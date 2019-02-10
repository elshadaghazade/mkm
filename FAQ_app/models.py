from django.db import models
from company_app.models import Companies
from django.contrib import admin


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(max_length=255)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = "Müəssisəyə tez-tez verilən sual"
        verbose_name_plural = "Müəssisəyə tez-tez verilən suallar"

class MainFaq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = "Tez-tez verilən sual"
        verbose_name_plural = "Tez-tez verilən suallar"


##### FAQ ADMIN #######
class FAQAdmin(admin.ModelAdmin):
    exclude = "company",

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.company = Companies.objects.get(profile=request.user)

        super(FAQAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(FAQAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(company=Companies.objects.get(profile=request.user))