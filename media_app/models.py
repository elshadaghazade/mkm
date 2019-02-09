from django.db import models
from company_app.models import Companies
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField

class CompanyPhotoGallery(models.Model):
    company = models.ForeignKey(Companies, verbose_name='Müəssisə', on_delete=models.CASCADE)
    photo_file = models.ImageField('Əsas şəkil', upload_to='media',default='')
    title = models.CharField('Başlıq', max_length=255)
    content = RichTextUploadingField('Kontent',
        config_name='special',
        external_plugin_resources=[(
            'youtube', 
            '/static/ckeditor/ckeditor/plugins/youtube/', 
            'plugin.js'
        ), 
        (
            'html5video',
            '/static/ckeditor/ckeditor/plugins/html5video_1.1/ckeditor-html5-video-master/html5video/',
            'plugin.js'
        )]
    )

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'Şəkil Qalereyası'
        verbose_name_plural = 'Şəkil Qalereyası'

class CompanyGalleryPhotos(models.Model):
    gallery = models.ForeignKey(CompanyPhotoGallery, on_delete=models.CASCADE)
    file = models.ImageField(verbose_name="Şəkil")

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = "Şəkil"
        verbose_name_plural = "Şəkillər"


class CompanyVideoGallery(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='media')
    title = models.CharField(max_length=255)
    content = RichTextUploadingField(
        config_name='special',
        external_plugin_resources=[(
            'youtube', 
            '/static/ckeditor/ckeditor/plugins/youtube/', 
            'plugin.js'
        ), 
        (
            'html5video',
            '/static/ckeditor/ckeditor/plugins/html5video_1.1/ckeditor-html5-video-master/html5video/',
            'plugin.js'
        )]
    )

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'Video Gallery'
        verbose_name_plural = 'Video Galleries'


#### admin ####

class CompanyGalleryPhotosInline(admin.TabularInline):
    model = CompanyGalleryPhotos

class CompanyPhotoGalleryAdmin(admin.ModelAdmin):
    exclude = "company",
    inlines = [CompanyGalleryPhotosInline]

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.company = Companies.objects.get(profile=request.user)
        super(CompanyPhotoGalleryAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(CompanyPhotoGalleryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(company=Companies.objects.get(profile=request.user))
