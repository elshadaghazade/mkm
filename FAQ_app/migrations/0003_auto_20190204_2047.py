# Generated by Django 2.1.5 on 2019-02-04 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ_app', '0002_mainfaq'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'Sual', 'verbose_name_plural': 'Tez-tez verilən suallar'},
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='company_id',
            new_name='company',
        ),
    ]
