# Generated by Django 2.1.5 on 2019-02-10 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_id', models.IntegerField(verbose_name='Region ID')),
                ('name', models.CharField(max_length=30, verbose_name='Regionun adı')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regionlar',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.IntegerField(verbose_name='Məktəb İD')),
                ('name', models.CharField(max_length=255, verbose_name='Məktəbin adı')),
                ('longitude', models.FloatField(default=0)),
                ('latitude', models.FloatField(default=0)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools_app.Regions')),
            ],
        ),
    ]
