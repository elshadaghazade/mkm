# Generated by Django 2.1.5 on 2019-02-10 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_news_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='type',
        ),
    ]
