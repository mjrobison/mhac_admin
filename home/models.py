from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.api import APIField


class HomePage(Page):
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null= True,
        blank=True,
        on_delete = models.SET_NULL , 

    )

    hero_title = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel("hero_image"),
        FieldPanel("hero_title")
    ]

    api_fields = [
        APIField('hero_image'),
        APIField('hero_title'),
    ]