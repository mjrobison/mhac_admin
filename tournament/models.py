from django.db import models

from wagtail.api import APIField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class tournamentPage(Page):
    year = models.CharField(max_length=4)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('year'),
        FieldPanel('body')
    ]

    api_fields = [
        APIField('body')
    ]