from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.templatetags.wagtailcore_tags import richtext


class LogoBlock(blocks.StructBlock):
    # text = blocks.TextBlock(Required=True, help_text="Your content goes here")
    logo = ImageChooserBlock(Required=True)


class ParagraphRichTextBlock(blocks.StructBlock):
    header = blocks.CharBlock(form_classname="Section Header", required=False, blank=True)
    displayHeader = blocks.BooleanBlock(required=False)
    section = blocks.CharBlock(required=False)

    content = blocks.RichTextBlock(Required=True, help_text="Add the page content here")

    # def get_api_representation(self, value, context=None):
    #     return richtext(value.source)

