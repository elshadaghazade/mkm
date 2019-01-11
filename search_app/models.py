from django.db import models
from company_app.models import Companies
# Create your models here.

# map_locations 1. id 2. coords (langitude, lotitude) 3. building_name (optional) 3. company_id


class MapLocations(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    building_name = models.CharField(max_length=25, null=True, blank=True)
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.building_name, self.company_id.company_name)
