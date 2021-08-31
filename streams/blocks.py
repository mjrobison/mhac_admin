from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.templatetags.wagtailcore_tags import richtext


class LogoBlock(blocks.StructBlock):
    # text = blocks.TextBlock(Required=True, help_text="Your content goes here")
    logo = ImageChooserBlock(Required=True)


class DocumentBlock(blocks.StructBlock):
    document = DocumentChooserBlock(required=False)


class ParagraphRichTextBlock(blocks.StructBlock):
    header = blocks.CharBlock(form_classname="Section Header", required=False, blank=True)
    displayHeader = blocks.BooleanBlock(required=False)
    content = blocks.RichTextBlock(Required=True, help_text="Add the page content here")