from typing import Literal

from ..base import BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text import RichTextNonToggleable, RichTextToggleable
from .base_text_block import BaseTextBlock


class Heading1CreateSchema(BaseBlockCreateSchema):
    type: Literal['heading_1'] = 'heading_1'
    heading_1: RichTextNonToggleable._schema


class Heading1RetrieveSchema(BaseBlockRetrieveSchema,
                             Heading1CreateSchema):
    ...


class ToggleHeading1CreateSchema(Heading1CreateSchema):
    heading_1: RichTextToggleable._schema


class ToggleHeading1RetrieveSchema(BaseBlockRetrieveSchema,
                                   ToggleHeading1CreateSchema):
    ...


class Heading1(BaseTextBlock):
    _create_chema = Heading1CreateSchema
    _retrieve_schema = Heading1RetrieveSchema
    _rich_text_type = RichTextNonToggleable
    _schematic_name = 'heading_1'


class ToggleHeading1(Heading1):
    _create_chema = ToggleHeading1CreateSchema
    _retrieve_schema = ToggleHeading1RetrieveSchema
    _rich_text_type = RichTextToggleable
