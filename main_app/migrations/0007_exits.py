# Generated by Django 2.1.5 on 2019-01-30 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_generalinformation_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('documents_file', models.FileField(upload_to='media')),
            ],
        ),
    ]
