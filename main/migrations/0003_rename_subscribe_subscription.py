# Generated by Django 4.1.3 on 2022-11-05 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_subscribe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribe',
            new_name='Subscription',
        ),
    ]
