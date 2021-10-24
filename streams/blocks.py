from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.core.blocks import ChoiceBlock, CharBlock, URLBlock
from wagtail.contrib.table_block.blocks import TableBlock


import requests

class LogoBlock(blocks.StructBlock):
    # text = blocks.TextBlock(Required=True, help_text="Your content goes here")
    logo = ImageChooserBlock(Required=True)


class DocumentBlock(blocks.StructBlock):
    document = DocumentChooserBlock(required=False)


class ParagraphRichTextBlock(blocks.StructBlock):
    header = blocks.CharBlock(form_classname="Section Header", required=False, blank=True)
    displayHeader = blocks.BooleanBlock(required=False)
    content = blocks.RichTextBlock(Required=True, help_text="Add the page content here")
    isHeaderLink = blocks.BooleanBlock(form_classname="Is Header a Link", required=False)
    headerLink = blocks.URLBlock(required=False)

class TableBlock(blocks.StructBlock):
    header = blocks.CharBlock(form_classname="Section Header", required=False, blank=True)
    displayHeader = blocks.BooleanBlock(required=False)
    isHeaderLink = blocks.BooleanBlock(form_classname="Is Header a Link", required=False)
    headerLink = blocks.URLBlock(required=False)
    content = TableBlock()

class ContentImageBlock(blocks.StructBlock):
    try:
        seasons = requests.get('http://localhost:8000/getSeasons')
        seasons = seasons.json()
        seasons = [(season['season_id'], season['season_name'] + ' ' + season['level']['name']) for season in seasons]
    except Exception as exc:
        seasons = [{
            'season_id': '',
            'season_name': '',
            'level': {
                'name': '',
                'id': ''
            }
        }]

    year = blocks.ChoiceBlock(choices=seasons) # CharBlock(max_length=4, null=True, blank=True)
    image = ImageChooserBlock(Required=True)
    image_location = blocks.ChoiceBlock(choices=[
                                                    ('content-left', 'Left'),
                                                    ('content-center', 'Center'),
                                                    ('content-right', 'Right'),
                                                ])

