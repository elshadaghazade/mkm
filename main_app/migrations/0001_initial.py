# Generated by Django 2.1.5 on 2019-02-10 07:41

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('attributes_file', models.FileField(upload_to='media')),
            ],
            options={
                'verbose_name': 'Atribut',
                'verbose_name_plural': 'Atributlar',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('documents_file', models.FileField(upload_to='media')),
            ],
            options={
                'verbose_name': 'Sənəd',
                'verbose_name_plural': 'Sənədlər',
            },
        ),
        migrations.CreateModel(
            name='MainInformativePages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Başlıq')),
                ('slug', models.SlugField(max_length=40, verbose_name='Slug')),
                ('short_description', models.TextField(max_length=255, verbose_name='Qısa təsvir')),
                ('full_content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Kontent')),
            ],
            options={
                'verbose_name': 'İnformativ səhifə',
                'verbose_name_plural': 'İnformativ səhifələr',
            },
        ),
        migrations.CreateModel(
            name='Speeches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('documents_file', models.FileField(upload_to='media')),
            ],
            options={
                'verbose_name': 'Çıxış',
                'verbose_name_plural': 'Çıxışlar',
            },
        ),
    ]
