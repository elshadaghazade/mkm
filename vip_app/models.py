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
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)
    vip_type = models.CharField(max_length=255,
                                choices=TYPE_CHOICES)
    full_name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
   
    

    def __str__(self):
        return "{},{}".format(self.full_name, self.short_description)


class VipDescription(models.Model):
    vip = models.ForeignKey(VIP,on_delete=models.CASCADE, related_name="descriptions")
    short_description = models.CharField(max_length=255)
    text = models.TextField()

