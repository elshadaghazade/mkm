from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class MainInformativePages(models.Model):
    title = models.CharField('Başlıq', max_length=255)
    slug = models.SlugField('Slug', max_length=40)
    short_description = models.TextField('Qısa təsvir', max_length=255)
    full_content = RichTextUploadingField('Kontent', config_name='special',
        external_plugin_resources=[(
            'youtube', 
            '/static/ckeditor/ckeditor/plugins/youtube/', 
            'plugin.js'
        ), 
        (
            'html5video',
            '/static/ckeditor/ckeditor/plugins/html5video_1.1/ckeditor-html5-video-master/html5video/',
            'plugin.js'
        )])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "İnformativ səhifə"
        verbose_name_plural = "İnformativ səhifələr"

class Documents(models.Model):
    title = models.CharField(max_length=255)
    documents_file = models.FileField(upload_to="media")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sənəd"
        verbose_name_plural = "Sənədlər"

class Attributes(models.Model):
    title = models.CharField(max_length=255)
    attributes_file = models.FileField(upload_to="media")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Atribut"
        verbose_name_plural = "Atributlar"