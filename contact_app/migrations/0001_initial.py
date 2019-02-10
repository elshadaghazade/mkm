# Generated by Django 2.1.5 on 2019-02-10 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company_app', '0002_auto_20190210_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.IntegerField(choices=[(1, 'Email'), (2, 'Telefon'), (4, 'Adres'), (5, 'Faks')], default=1)),
                ('contact', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Müəssisənin əlaqə məlumatı',
                'verbose_name_plural': 'Müəssisənin əlaqə məlumatları',
            },
        ),
        migrations.CreateModel(
            name='ContactCompanyForm',
            fields=[
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='company_app.Companies')),
                ('to_email', models.EmailField(max_length=254, verbose_name='Kimə')),
                ('name_placeholder', models.CharField(default='Adınızı daxil edin', max_length=255, verbose_name='Ad üçün qeyd')),
                ('email_placeholder', models.CharField(default='Email adresinizi daxil edin', max_length=255, verbose_name='Email üçün qeyd')),
                ('subject_placeholder', models.CharField(default='Məktubun mövzusunu daxil edin', max_length=255, verbose_name='Mövzu üçün qeyd')),
                ('content_placeholder', models.CharField(default='Məktubun mətnini daxil edin', max_length=1000, verbose_name='Mətn üçün qeyd')),
            ],
            options={
                'verbose_name': 'Müəssisənin əlaqə formasının ayarları',
                'verbose_name_plural': 'Müəssisənin əlaqə formasının ayarları',
            },
        ),
        migrations.CreateModel(
            name='ContactCompanyReceivedEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=1000)),
                ('from_email', models.EmailField(max_length=254)),
                ('sent', models.BooleanField(default=False)),
                ('sent_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Müəssisəyə gələn məktub',
                'verbose_name_plural': 'Müəssisəyə gələn məktublar',
            },
        ),
        migrations.CreateModel(
            name='ContactMainForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_email', models.EmailField(max_length=254)),
                ('subject_placeholder', models.CharField(max_length=255)),
                ('content_placeholder', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMainReceivedEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=1000)),
                ('from_email', models.EmailField(max_length=254)),
                ('sent', models.EmailField(max_length=254)),
                ('sent_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
