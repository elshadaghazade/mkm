# Generated by Django 2.1.5 on 2019-01-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0007_auto_20190115_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyphotogallery',
            name='photo_file',
            field=models.FileField(upload_to='media'),
        ),
    ]
