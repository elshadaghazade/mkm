from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField


class Companies(models.Model):
    company_name = models.CharField('Müəssisənin adı', max_length=255)
    about = RichTextUploadingField('Haqqımızda', blank=True,
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
    main_duties = RichTextUploadingField('Əsas vəzifələr', blank=True,
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
    administration = RichTextUploadingField('Rəhbərlik', blank=True,
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
    achievements = RichTextUploadingField('Nailiyyətlərimiz', blank=True,
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
    admission_requirements = RichTextUploadingField('Qəbul qaydaları', blank=True,
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
    address = models.CharField('Adres', max_length=255, blank=True)
    phone_number = models.CharField('Telefon', max_length=25, blank=True)
    about_images = models.ImageField('Şəkil', upload_to='media', blank=True) 
    main_activity = models.CharField('Fəaliyyət', max_length=255, blank=True)
    profile = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Müəssisə'
        verbose_name_plural = 'Müəssisələr'

class CompanyActivityAreas(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    area = models.CharField('Fəaliyyət sahəsi', max_length=255)

    def __str__(self):
        return self.area

    class Meta:
        verbose_name = "Fəaliyyət sahəsi"
        verbose_name_plural = "Fəaliyyət sahələri"

class CompanyActivityLocations(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    activity_location = models.CharField('Yerləşdiyi məkan', max_length=255)

    def __str__(self):
        return self.activity_location

    class Meta:
        verbose_name = 'Təşkil olunduğu yer'
        verbose_name_plural = 'Təşkil olunduğu yerlər'

# class CompanyAdministration(models.Model):
#     company = models.ForeignKey(Companies, on_delete=models.CASCADE)
#     # parent = models.ForeignKey(self, on_delete=models.CASCADE, null=True)
#     #about_images = models.ImageField(upload_to='media') 
#     full_name = models.CharField('Adı və soyadı', max_length=255)
#     occupation = models.CharField('Tutduğu vəzifə', max_length=255)
#     administration_type = models.CharField('İdarə növü', max_length=255)
#     branch_icon = models.ImageField('Filialın emblemi', upload_to='media')

#     def __str__(self):
#         return "{}".format(self.full_name)

#     class Meta:
#         verbose_name = "Rəhbərlik"
#         verbose_name_plural = "Rəhbərlik"


class CompanyInformativePages(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40)
    short_description = models.CharField(max_length=255)
    full_content = RichTextUploadingField(
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
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "İnformativ səhifə"
        verbose_name_plural = "İnformativ səhifələr"


#### admin #####

# class CompanyAdministrationAdmin(admin.ModelAdmin):
#     exclude = "company",

#     def save_model(self, request, obj, form, change):
#         if not request.user.is_superuser:
#             obj.company = Companies.objects.get(profile=request.user)

#         super(CompanyAdministrationAdmin, self).save_model(request, obj, form, change)

#     def get_queryset(self, request):
#         qs = super(CompanyAdministrationAdmin, self).get_queryset(request)

#         if request.user.is_superuser:
#             return qs

#         return qs.filter(company=Companies.objects.get(profile=request.user))


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

class CompanyActivityAreasInline(admin.TabularInline):
    model = CompanyActivityAreas
    extra=1

class CompanyActivityLocationsInline(admin.TabularInline):
    model = CompanyActivityLocations
    extra = 1

class CompaniesAdmin(admin.ModelAdmin):
    # exclude = 'profile',
    inlines = [CompanyActivityLocationsInline, CompanyActivityAreasInline]

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.profile = request.user
        super(CompaniesAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(CompaniesAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(profile=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "profile" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(pk=request.user.id)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_inline_instances(self, request, obj=None):
        return [inline(self.model, self.admin_site) for inline in self.inlines]

