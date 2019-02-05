# Generated by Django 2.1.5 on 2019-02-03 08:56

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0035_auto_20190202_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyActivityAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=255, verbose_name='Fəaliyyət sahəsi')),
            ],
        ),
        migrations.AlterField(
            model_name='companies',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Haqqımızda'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='about_images',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Şəkil'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='admission_requirements',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Qəbul qaydaları'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='company_name',
            field=models.CharField(max_length=255, verbose_name='Müəssisənin adı'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='main_activity',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Fəaliyyət'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='main_duties',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Əsas vəzifələr'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='phone_number',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='companyadministration',
            name='administration_type',
            field=models.CharField(max_length=255, verbose_name='İdarə növü'),
        ),
        migrations.AlterField(
            model_name='companyadministration',
            name='branch_icon',
            field=models.ImageField(upload_to='media', verbose_name='Filialın emblemi'),
        ),
        migrations.AlterField(
            model_name='companyadministration',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='Adı və soyadı'),
        ),
        migrations.AlterField(
            model_name='companyadministration',
            name='occupation',
            field=models.CharField(max_length=255, verbose_name='Tutduğu vəzifə'),
        ),
        migrations.AlterField(
            model_name='companyphotogallery',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_app.Companies', verbose_name='Müəssisə'),
        ),
        migrations.AlterField(
            model_name='companyphotogallery',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Kontent'),
        ),
        migrations.AlterField(
            model_name='companyphotogallery',
            name='photo_file',
            field=models.ImageField(default='', upload_to='media', verbose_name='Şəkil'),
        ),
        migrations.AlterField(
            model_name='companyphotogallery',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Başlıq'),
        ),
        migrations.AddField(
            model_name='companyactivityareas',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_app.Companies'),
        ),
    ]
