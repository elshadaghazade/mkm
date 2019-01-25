# Generated by Django 2.1.5 on 2019-01-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_auto_20190124_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companynews',
            old_name='full_content',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='full_description',
            new_name='full_content',
        ),
        migrations.RemoveField(
            model_name='news',
            name='text',
        ),
        migrations.AddField(
            model_name='companynews',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]