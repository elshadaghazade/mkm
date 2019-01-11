from django.db import models

# Create your models here.
class InformativPages(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40)
    short_description = models.CharField(max_length=255)
    full_content = models.CharField(max_length=255)

    def __str__(self):
        return "{},{},{}".format(self.title,self.short_description,self.full_content)
