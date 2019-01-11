from django.db import models
from company_app.models import Companies


# Create your models here.
class VIP(models.Model):
    MEDAL_ALANLAR = 'MA'  # Medal Alanlar
    FERQLENENLER = 'FQ'  # Ferqlenenler
    TYPE_CHOICES = (
        (MEDAL_ALANLAR, 'medal_alanlar'),
        (FERQLENENLER, 'ferqlenenler')
    )

    full_name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    vip_type = models.CharField(max_length=255,
                                choices=TYPE_CHOICES)
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return "{},{}".format(self.full_name, self.short_description)
