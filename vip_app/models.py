from django.db import models
from company_app.models import Companies
# Create your models here.
class VIP(models.Model):
    full_name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    MEDAL_ALANLAR = 'MEDAL_ALANLAR'
    FERQLENENLER = 'FERQLENENLER'
    TYPE_CHOICES=(
         (MEDAL_ALANLAR, 'medal_alanlar'),
         (FERQLENENLER, 'ferqlenenler')
     )
    vip_type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return "{},{}".format(self.full_name,self.short_description)