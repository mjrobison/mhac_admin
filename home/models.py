from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.api.fields import ImageRenditionField
from wagtail.api import APIField


class HomePage(Page):

    max_count=1
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    tagline_line1 = models.CharField(max_length=150, blank=True, null=True)
    tagline_line2 = models.CharField(max_length=150, blank=True, null=True)
    message = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel("hero_image"),
        FieldPanel("message"),
        MultiFieldPanel([
            FieldPanel('tagline_line1'),
            FieldPanel('tagline_line2')
        ], 'Tagline')
    ]

    api_fields = [
        APIField('hero_image'),# serializer=ImageRenditionField(filter_spec='full')),
        APIField('message'),
        APIField('tagline_line1'),
        APIField('tagline_line2'),
    ]