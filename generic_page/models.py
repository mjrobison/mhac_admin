from django.db import models

from wagtail.api import APIField
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail_headless_preview.models import HeadlessPreviewMixin

from streams import blocks


class GenericPage(HeadlessPreviewMixin, Page):

    content = StreamField(
        [
            ("team_image_block", blocks.LogoBlock()),
            ("page_content", blocks.ParagraphRichTextBlock()),
            ("content_image", blocks.ContentImageBlock()),

        ],
        null=True, blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content')
    ]

    api_fields = [
        APIField('content')
    ]