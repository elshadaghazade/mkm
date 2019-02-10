# Generated by Django 2.1.5 on 2019-02-09 22:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_app', '0008_auto_20190209_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companygalleryphotos',
            name='file',
            field=models.ImageField(upload_to='company_gallery_photos', verbose_name='Şəkil'),
        ),
        migrations.AlterField(
            model_name='companygalleryvideos',
            name='file',
            field=models.FileField(upload_to='company_gallery_videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'mpeg'])], verbose_name='Video fayl'),
        ),
        migrations.AlterField(
            model_name='companyphotogallery',
            name='photo_file',
            field=models.ImageField(default='', upload_to='company_gallery_photo', verbose_name='Əsas şəkil'),
        ),
    ]
