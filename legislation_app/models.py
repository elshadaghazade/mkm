from django.db import models
from company_app.models import Companies

class Legislation(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    legislation_file = models.FileField(upload_to="media")