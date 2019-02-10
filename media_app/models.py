from django.db import models
from company_app.models import Companies
from django.core.validators import FileExtensionValidator
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField

class CompanyPhotoGallery(models.Model):
    company = models.ForeignKey(Companies, verbose_name='Müəssisə', on_delete=models.CASCADE)
    photo_file = models.ImageField('Əsas şəkil', upload_to='company_gallery_photo',default='')
    title = models.CharField('Başlıq', max_length=255)
    content = RichTextUploadingField('Qalereyanın mətni',
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
    file = models.ImageField(verbose_name="Şəkil", upload_to='company_gallery_photos')

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = "Şəkil"
        verbose_name_plural = "Şəkillər"


class CompanyVideoGallery(models.Model):
    company = models.ForeignKey(Companies, verbose_name='Müəssisə', on_delete=models.CASCADE)
    photo_file = models.ImageField('Əsas şəkil', upload_to='company_video_gallery_photo',default='')
    title = models.CharField(max_length=255)
    content = RichTextUploadingField(
        verbose_name='Qalereyanın mətni',
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
        return self.title

    class Meta:
        verbose_name = 'Video Qalereya'
        verbose_name_plural = 'Video Qalereyalar'


class CompanyGalleryVideos(models.Model):
    gallery = models.ForeignKey(CompanyVideoGallery, on_delete=models.CASCADE)
    file = models.FileField(verbose_name="Video fayl", upload_to='company_gallery_videos', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'mpeg'])])

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videolar"


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


class CompanyGalleryVideosInline(admin.TabularInline):
    model = CompanyGalleryVideos
    extra = 5

class CompanyVideoGalleryAdmin(admin.ModelAdmin):
    exclude = "company",
    inlines = [CompanyGalleryVideosInline]

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.company = Companies.objects.get(profile=request.user)
        super(CompanyVideoGalleryAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(CompanyVideoGalleryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(company=Companies.objects.get(profile=request.user))