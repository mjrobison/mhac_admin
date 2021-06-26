from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.api import APIField
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail_headless_preview.models import HeadlessPreviewMixin
from streams import blocks


class AboutStreamFields(HeadlessPreviewMixin, Page):
    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # content = StreamField(
    #     [
    #         ("about_paragraph", blocks.ParagraphRichTextBlock()),
    #         ("document", blocks.DocumentBlock())
    #
    #     ],
    #     null=True, blank=True
    # )

    content_panels = Page.content_panels + [
        InlinePanel("section")
        # StreamFieldPanel('content'),
        # MultiFieldPanel(
        #     [InlinePanel("content_order", max_num=5, min_num=1, label="Image")],
        #     heading="Content Section",
        # ),
    ]


    api_fields = [
        APIField('section')
    ]


class AboutPageContent(Orderable):
    page = ParentalKey(AboutStreamFields, on_delete=models.CASCADE, related_name='section')
    displaySectionTitle = models.BooleanField(default=True)
    sectionHeader = models.CharField(null=True, blank=True, max_length=150)
    content = StreamField(
        [
            ("about_paragraph", blocks.ParagraphRichTextBlock()),
            # ("document", blocks.DocumentBlock())

        ],
        null=True, blank=True
    )
    panels = [
        FieldPanel('sectionHeader'),
        FieldPanel('displaySectionTitle'),
        StreamFieldPanel('content')
    ]

    api_fields = [
        APIField('displaySectionTitle'),
        APIField('sectionHeader'),
        APIField('content'),
    ]


