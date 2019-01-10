from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CompanyProfile(models.Model):
    profile_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.profile_id)


class Companies(models.Model):
    company_name = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    main_activity = models.CharField(max_length=255)
    regulation_file = models.FileField(upload_to='media')
    admission_requirements = models.CharField(max_length=255)
    profile_id = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

    def __str__(self):
        return "{},{},{},{},{}".format(self.company_name,
                                       self.about,
                                       self.main_activity,
                                       self.regulation_file,
                                       self.admission_requirements)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Administration(models.Model):
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)
    parent_id = models.IntegerField()
    full_name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    administration_type = models.CharField(max_length=255)
    branch_icon = models.FileField(upload_to='media')

    def __str__(self):
        return "{},{},{}".format(self.full_name,
                                 self.occupation,
                                 self.administration_type)


class PhotoGallery(models.Model):
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)
    photo_file = models.FileField(upload_to='media')
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return "{},{}".format(self.title, self.content)

    class Meta:
        verbose_name = 'Photo Gallery'
        verbose_name_plural = 'Photo Galleries'


class VideoGallery(models.Model):
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='media')
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return "{},{}".format(self.title, self.content)

    class Meta:
        verbose_name = 'Video Gallery'
        verbose_name_plural = 'Video Galleries'
