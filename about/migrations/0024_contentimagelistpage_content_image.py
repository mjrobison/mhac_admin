# Generated by Django 3.1.11 on 2021-09-12 22:58

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0023_contentimagelistpage_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentimagelistpage',
            name='content_image',
            field=wagtail.core.fields.StreamField([('content_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(Required=True)), ('image_location', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))], blank=True, null=True),
        ),
    ]
