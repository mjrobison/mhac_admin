# Generated by Django 3.1.11 on 2021-06-13 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210613_0351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='hero_title',
            new_name='message',
        ),
    ]