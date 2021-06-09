from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class LogoBlock(blocks.StructBlock):
    # text = blocks.TextBlock(Required=True, help_text="Your content goes here")
    logo = ImageChooserBlock(Required=True)


class ParagraphRichTextBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(Required=True, help_text="Add the page content here")
