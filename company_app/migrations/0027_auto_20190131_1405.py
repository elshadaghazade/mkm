# Generated by Django 2.1.5 on 2019-01-31 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0026_auto_20190131_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyphotogallery',
            old_name='company_id',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='companyvideogallery',
            old_name='company_id',
            new_name='company',
        ),
    ]
