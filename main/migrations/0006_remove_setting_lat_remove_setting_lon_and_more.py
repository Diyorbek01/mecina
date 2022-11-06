# Generated by Django 4.1.3 on 2022-11-05 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_setting_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='lon',
        ),
        migrations.AddField(
            model_name='setting',
            name='location',
            field=models.CharField(default='https://goo.gl/maps/KioPR6wRze1gszdE6', max_length=300, verbose_name='Location'),
            preserve_default=False,
        ),
    ]
