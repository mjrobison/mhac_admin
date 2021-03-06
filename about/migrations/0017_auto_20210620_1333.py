# Generated by Django 3.1.11 on 2021-06-20 13:33

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0016_aboutpagecontent_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpagecontent',
            name='sectionHeader',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='aboutpagecontent',
            name='content',
            field=wagtail.core.fields.StreamField([('about_paragraph', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(blank=True, form_classname='Section Header', required=False)), ('displayHeader', wagtail.core.blocks.BooleanBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(Required=True, help_text='Add the page content here'))]))], blank=True, null=True),
        ),
    ]
