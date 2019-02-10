from django.db import models
from company_app.models import Companies
from django.contrib import admin
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.category_name)

    class Meta:
        verbose_name = "Xəbərin Kateqoriyası"
        verbose_name_plural = "Kateqoriyalar"


class News(models.Model):
    title = models.CharField(max_length=255)
    news_picture = models.ImageField(upload_to='media')
    short_description = models.TextField(max_length=255)
    long_description = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}".format(self.title)

class CompanyNews(models.Model):
    title = models.CharField("Başlıq", max_length=255)
    news_picture = models.ImageField(upload_to='media', verbose_name="Xəbərin əsas şəkli")
    short_description = models.TextField("Qısa təsvir", max_length=255)
    text = RichTextUploadingField('Xəbərin mətni',
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_date = models.DateTimeField()
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)


    class Meta:
        verbose_name = "MÜəssisənin xəbəri"
        verbose_name_plural = "Müəssisənin xəbərləri"


class CompanyNewsSlideImages(models.Model):
    company_news = models.ForeignKey(CompanyNews, verbose_name='Xəbər', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Xəbər üçün slayd şəkli', upload_to='company_news_slides')
    weight = models.IntegerField('Şəklin sırası', default=1)

    class Meta:
        verbose_name = 'Slayd üçün şəkil'
        verbose_name_plural = 'Slayd üçün şəkillər'

#### admin models #####

class CategoryAdmin(admin.ModelAdmin):
    fields = "category_name",

    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(profile=request.user)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.profile = request.user
        super().save_model(request, obj, form, change)


class CompanyNewsSlideImagesInline(admin.TabularInline):
    model = CompanyNewsSlideImages
    extra=5

class CompanyNewsAdmin(admin.ModelAdmin):
    fields = "title", "news_picture", "short_description", "text", "category", "publish_date"
    list_filter = 'title', 'category'
    inlines = [CompanyNewsSlideImagesInline]

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.company = Companies.objects.get(profile=request.user)
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(CompanyNewsAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(company=Companies.objects.get(profile=request.user.id))

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(profile=request.user)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_inline_instances(self, request, obj=None):
        return [inline(self.model, self.admin_site) for inline in self.inlines]