# Generated by Django 2.1.5 on 2019-01-31 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0007_category_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Xəbərin Kateqoriyası', 'verbose_name_plural': 'Kateqoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='companynews',
            options={'verbose_name': 'Xəbər', 'verbose_name_plural': 'Xəbərlər'},
        ),
    ]
