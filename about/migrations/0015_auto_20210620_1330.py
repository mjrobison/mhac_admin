# Generated by Django 3.1.11 on 2021-06-20 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0014_auto_20210620_1330'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPageRelatedLink',
            new_name='AboutPageContent',
        ),
    ]