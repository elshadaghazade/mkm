# Generated by Django 2.1.5 on 2019-01-24 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0018_remove_companies_legislation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='admission_requirements',
            field=models.TextField(),
        ),
    ]
