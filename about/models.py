from django.db import models

from wagtail.api import APIField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail_headless_preview.models import HeadlessPreviewMixin
from streams import blocks


class AboutPage(HeadlessPreviewMixin, Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]

    api_fields = [
        APIField('body')
    ]


class AboutStreamFields(HeadlessPreviewMixin, Page):

    content = StreamField(
        [
            ("about_paragraph", blocks.ParagraphRichTextBlock())
        ]
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content')
    ]