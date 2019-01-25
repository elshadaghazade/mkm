from django.db import models
from company_app.models import Companies
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.category_name)


class NewsCategories(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class News(models.Model):
    title = models.CharField(max_length=255)
    news_picture = models.ImageField(upload_to='media')
    short_description = models.CharField(max_length=255)
    full_content = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now=True)

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
