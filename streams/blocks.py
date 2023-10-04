from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.core.blocks import ChoiceBlock, CharBlock, URLBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField


from django.conf import settings

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
    # try:
    seasons = requests.get(f'{settings.BASE_API_URL}/getSeasons')
    seasons = seasons.json()
    seasons = [(f"{season['season_name']} {season['level']}", f"{season['season_name']} {season['level']}") for season in seasons]


    teams = requests.get(f'{settings.BASE_API_URL}/getTeams')
    teams = teams.json()
    teams = [(f"{team['team_name']} {team['team_mascot']}", f"{team['team_name']} {team['team_mascot']}") for team in teams]

    year = ChoiceBlock(choices=seasons)
    team = ChoiceBlock(choices=teams)
    image = ImageChooserBlock(Required=True)
    image_location = ChoiceBlock(choices=[
                                                    ('content-left', 'Left'),
                                                    ('content-center', 'Center'),
                                                    ('content-right', 'Right'),
                                                ])
    api_fields = [
        APIField('year'),
        APIField('team'),
        APIField('image_location'),
        APIField('image', serializer=ImageRenditionField('fill-200x250', source='image'))
    ]

    def get_api_representation(self, value, context=None):
        """ Recursively call get_api_representation on children and return as a plain dict """
        new_dict = {}
        new_dict['year'] = value.get('year')
        new_dict['team'] = value.get('team')
        new_dict['image_location'] = value.get('image_location')
        new_dict['image_url'] = value.get('image').file.url


        return new_dict

class LeftContentImageBlock(blocks.StructBlock):
    # try:
    seasons = requests.get(f'{settings.BASE_API_URL}/getSeasons')
    seasons = seasons.json()
    seasons = [(f"{season['season_name']} {season['level']}", f"{season['season_name']} {season['level']}") for season in seasons]


    teams = requests.get(f'{settings.BASE_API_URL}/getTeams')
    teams = teams.json()
    teams = [(f"{team['team_name']} {team['team_mascot']}", f"{team['team_name']} {team['team_mascot']}") for team in teams]

    year = ChoiceBlock(choices=seasons)
    team = ChoiceBlock(choices=teams)
    image = ImageChooserBlock(Required=True)

    def get_api_representation(self, value, context=None):
        """ Recursively call get_api_representation on children and return as a plain dict """
        new_dict = {}
        new_dict['year'] = value.get('year')
        new_dict['team'] = value.get('team')
        new_dict['image_location'] = 'content-left'
        new_dict['image_url'] = value.get('image').file.url


        return new_dict

class RightContentImageBlock(blocks.StructBlock):
    # try:
    seasons = requests.get(f'{settings.BASE_API_URL}/getSeasons')
    seasons = seasons.json()
    seasons = [(f"{season['season_name']} {season['level']}", f"{season['season_name']} {season['level']}") for season in seasons]


    teams = requests.get(f'{settings.BASE_API_URL}/getTeams')
    teams = teams.json()
    teams = [(f"{team['team_name']} {team['team_mascot']}", f"{team['team_name']} {team['team_mascot']}") for team in teams]

    year = ChoiceBlock(choices=seasons)
    team = ChoiceBlock(choices=teams)
    image = ImageChooserBlock(Required=True)

    def get_api_representation(self, value, context=None):
        """ Recursively call get_api_representation on children and return as a plain dict """
        new_dict = {}
        new_dict['year'] = value.get('year')
        new_dict['team'] = value.get('team')
        new_dict['image_location'] = 'content-right'
        new_dict['image_url'] = value.get('image').file.url


        return new_dict




