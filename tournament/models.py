from django.db import models

from wagtail.api import APIField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel


# class tournamentPage(Page):
#     # year = models.CharField(max_length=4)
#     # body = RichTextField(blank=True)
#
#     tournament_information = RichTextField(blank=True)
#     tournament_packet = models.ForeignKey(
#         'wagtaildocs.Document',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )
#     content_panels = Page.content_panels + [
#         # FieldPanel('year'),
#         FieldPanel('tournament_information'),
#         DocumentChooserPanel('tournament_packet'),
#     ]
#
#     api_fields = [
#         APIField('tournament_information')
#     ]