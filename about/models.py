from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.api import APIField
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
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

    content_panels = Page.content_panels + [
        InlinePanel("section")
    ]

    api_fields = [
        APIField('section')
    ]


class AboutPageContent(Orderable):
    page = ParentalKey(AboutStreamFields, on_delete=models.CASCADE, related_name='section')
    displaySectionTitle = models.BooleanField(default=True)
    sectionHeader = models.CharField(null=True, blank=True, max_length=150)
    content = RichTextField(null=True, blank=True)

    subsections = StreamField(
        [
            ("about_paragraph", blocks.ParagraphRichTextBlock()),
            ("table_block", blocks.TableBlock())

        ],
        null=True, blank=True, use_json_field=True
    )
    panels = [
        FieldPanel('sectionHeader'),
        FieldPanel('displaySectionTitle'),
        FieldPanel('content'),
        FieldPanel('subsections')
    ]

    api_fields = [
        APIField('displaySectionTitle'),
        APIField('sectionHeader'),
        APIField('content'),
        APIField('subsections')
    ]


# class ContentImageListPage(Page):
#     year = models.CharField(max_length=4, null=False, blank=False)
#     # content_image = blocks.ContentImageBlock()
#     content_image = StreamField(
#         [
#             ("content_image", blocks.ContentImageBlock()),
#
#         ],
#         null=True, blank=True
#     )
#     panels = [
#         StreamFieldPanel(content_image)
#     ]
#
