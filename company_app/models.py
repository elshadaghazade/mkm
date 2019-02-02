from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField


class Companies(models.Model):
    company_name = models.CharField(max_length=255)
    about = RichTextUploadingField(
        config_name='default',
        external_plugin_resources=[('youtube', '/static/base/vendor/ckeditor_plugins/youtube/youtube/', 'plugin.js')]
    )
    main_duties = RichTextUploadingField()
    about_images = models.ImageField(upload_to='media') 
    main_activity = models.CharField(max_length=255)
    admission_requirements = RichTextUploadingField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.company_name)

    class Meta:
        verbose_name = 'Müəssisə'
        verbose_name_plural = 'Müəssisələr'


class CompanyAdministration(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    # parent = models.ForeignKey(self, on_delete=models.CASCADE, null=True)
    #about_images = models.ImageField(upload_to='media') 
    full_name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    administration_type = models.CharField(max_length=255)
    branch_icon = models.FileField(upload_to='media')

    def __str__(self):
        return "{}".format(self.full_name)

    class Meta:
        verbose_name = "Rəhbərlik"
        verbose_name_plural = "Rəhbərlik"

class CompanyGalleryPhotos(models.Model):
    file = models.ImageField(verbose_name="Şəkil")

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = "Şəkil"
        verbose_name_plural = "Şəkillər"

class CompanyPhotoGallery(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    photo_file = models.FileField(upload_to='media',default='')
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    photo = models.ManyToManyField(CompanyGalleryPhotos)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'Şəkil Qalereyası'
        verbose_name_plural = 'Şəkil Qalereyası'


class CompanyVideoGallery(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='media')
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'Video Gallery'
        verbose_name_plural = 'Video Galleries'


class CompanyInformativePages(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40)
    short_description = models.CharField(max_length=255)
    full_content = RichTextUploadingField()
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "İnformativ səhifə"
        verbose_name_plural = "İnformativ səhifələr"


#### admin #####

class CompanyAdministrationAdmin(admin.ModelAdmin):
    exclude = "company",

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.company = Companies.objects.get(profile=request.user)

        super(CompanyAdministrationAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(CompanyAdministrationAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(company=Companies.objects.get(profile=request.user))


class CompanyInformativePagesAdmin(admin.ModelAdmin):
    exclude = "company",

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.company = Companies.objects.get(profile=request.user)
        super(CompanyInformativePagesAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(CompanyInformativePagesAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(company=Companies.objects.get(profile=request.user))

class CompanyPhotoGalleryAdmin(admin.ModelAdmin):
    exclude = "company",

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.company = Companies.objects.get(profile=request.user)
        super(CompanyPhotoGalleryAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(CompanyPhotoGalleryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(company=Companies.objects.get(profile=request.user))


class CompaniesAdmin(admin.ModelAdmin):
    exclude = 'profile',

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.profile = request.user
        super(CompaniesAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(CompaniesAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(profile=request.user)

