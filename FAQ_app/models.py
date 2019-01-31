from django.db import models
from company_app.models import Companies
# Create your models here.


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return "{},{}".format(self.question,self.answer)

class MainFaq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return "{},{}".format(self.question,self.answer)