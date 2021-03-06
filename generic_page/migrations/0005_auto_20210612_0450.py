# Generated by Django 3.1.11 on 2021-06-12 04:50

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('generic_page', '0004_auto_20210529_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='content',
            field=wagtail.core.fields.StreamField([('team_image_block', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(Required=True))])), ('page_content', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(form_classname='Section Header')), ('text', wagtail.core.blocks.RichTextBlock(Required=True, help_text='Add the page content here'))]))], blank=True, null=True),
        ),
    ]
