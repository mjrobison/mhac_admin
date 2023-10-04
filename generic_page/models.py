from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.api import APIField
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail_headless_preview.models import HeadlessPreviewMixin
from django.conf import settings
from streams import blocks


class GenericPage(Page):

    content_panels = Page.content_panels + [
        InlinePanel('champsList', max_num=1)
    ]

    api_fields = [
        APIField('champsList')
    ]
    


class ChampionPageContent(Orderable):
    page = ParentalKey(GenericPage, on_delete=models.CASCADE, related_name='champsList')

    content = StreamField(
        [
            ("content_left", blocks.LeftContentImageBlock()),
            ("content_right", blocks.RightContentImageBlock())

        ],
        null=True, blank=True, use_json_field=True
    )

    panels = [
        FieldPanel('content')
    ]

    api_fields = [
        APIField('content')
    ]
