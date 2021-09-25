# Generated by Django 3.1.11 on 2021-09-12 23:05

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('generic_page', '0009_auto_20210912_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='content',
            field=wagtail.core.fields.StreamField([('team_image_block', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(Required=True))])), ('page_content', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(blank=True, form_classname='Section Header', required=False)), ('displayHeader', wagtail.core.blocks.BooleanBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(Required=True, help_text='Add the page content here'))])), ('content_image', wagtail.core.blocks.StructBlock([('year', wagtail.core.blocks.CharBlock(blank=True, max_length=4, null=True)), ('image', wagtail.images.blocks.ImageChooserBlock(Required=True)), ('image_location', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))], blank=True, null=True),
        ),
    ]
