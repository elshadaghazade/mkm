from django.db import models


# Create your models here.
class MainInformativePages(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40)
    short_description = models.CharField(max_length=255)
    full_content = models.CharField(max_length=255)

    def __str__(self):
        return "{},{},{}".format(self.title, self.short_description, self.full_content)

class Documents(models.Model):
    title = models.CharField(max_length=255)
    documents_file = models.FileField(upload_to="media")

    def __str__(self):
        return "{} {}".format(self.title,self.documents_file)

class Attributes(models.Model):
    title = models.CharField(max_length=255)
    attributes_file = models.FileField(upload_to="media")

    def __str__(self):
        return "{} {}".format(self.title,self.attributes_file)
    
class GeneralInformation(models.Model):
    text = models.TextField()

    def __str__(self):
        return "{}".format(self.text)

class Exits(models.Model):
    title = models.CharField(max_length=255)
    documents_file = models.FileField(upload_to="media")

    def __str__(self):
        return "{} {}".format(self.title,self.documents_file)