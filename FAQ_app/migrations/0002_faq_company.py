# Generated by Django 2.1.5 on 2019-02-10 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company_app', '0001_initial'),
        ('FAQ_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_app.Companies'),
        ),
    ]