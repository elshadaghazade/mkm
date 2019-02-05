# Generated by Django 2.1.5 on 2019-02-04 19:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0049_auto_20190204_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='Haqqımızda'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companies',
            name='about_images',
            field=models.ImageField(blank=True, default='', upload_to='media', verbose_name='Şəkil'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companies',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Adres'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companies',
            name='administration',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='Rəhbərlik'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companies',
            name='admission_requirements',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='Qəbul qaydaları'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companies',
            name='main_activity',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Fəaliyyət'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companies',
            name='main_duties',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='Əsas vəzifələr'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companies',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='Telefon'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companies',
            name='url',
            field=models.URLField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
