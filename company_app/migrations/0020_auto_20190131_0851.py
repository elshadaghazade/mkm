# Generated by Django 2.1.5 on 2019-01-31 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0019_auto_20190124_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
