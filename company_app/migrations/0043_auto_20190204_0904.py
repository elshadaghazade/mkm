# Generated by Django 2.1.5 on 2019-02-04 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0042_auto_20190204_0837'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompanyLocations',
            new_name='CompanyYerler',
        ),
        migrations.RenameField(
            model_name='companyyerler',
            old_name='location',
            new_name='yer',
        ),
    ]
