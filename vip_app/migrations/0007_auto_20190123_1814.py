# Generated by Django 2.1.5 on 2019-01-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vip_app', '0006_auto_20190122_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vipdescription',
            name='vip',
        ),
        migrations.AddField(
            model_name='vip',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='VipDescription',
        ),
    ]