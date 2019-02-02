from django.db import models
from company_app.models import Companies
from django.contrib import admin
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.category_name)

    class Meta:
        verbose_name = "Xəbərin Kateqoriyası"
        verbose_name_plural = "Kateqoriyalar"

class NewsCategories(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class News(models.Model):
    title = models.CharField(max_length=255)
    news_picture = models.ImageField(upload_to='media')
    short_description = models.CharField(max_length=255)
    long_description = models.CharField(max_length=255)
    text = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}".format(self.title)

class CompanyNews(models.Model):
    title = models.CharField(max_length=255)
    news_picture = models.ImageField(upload_to='media')
    short_description = models.CharField(max_length=255)
    long_description = models.CharField(max_length=255)
    text = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_date = models.DateTimeField()
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)


    class Meta:
        verbose_name = "Xəbər"
        verbose_name_plural = "Xəbərlər"


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

class CompanyNewsAdmin(admin.ModelAdmin):
    fields = "title", "news_picture", "short_description", "long_description", "text", "category_id", "publish_date"
    list_filter = 'title', 'category_id'

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.company_id = Companies.objects.get(profile_id=request.user.id)
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(CompanyNewsAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(company_id=Companies.objects.get(profile_id=request.user.id))

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        
        if db_field.name == "category_id":
            kwargs["queryset"] = Category.objects.filter(profile=request.user)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)