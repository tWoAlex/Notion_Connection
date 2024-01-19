from typing import Literal

from ..base import BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text import RichTextNonToggleable, RichTextToggleable
from .base_text_block import BaseTextBlock


class Heading3CreateSchema(BaseBlockCreateSchema):
    type: Literal['heading_3'] = 'heading_3'
    heading_3: RichTextNonToggleable._schema


class Heading3RetrieveSchema(BaseBlockRetrieveSchema,
                             Heading3CreateSchema):
    ...


class ToggleHeading3CreateSchema(Heading3CreateSchema):
    heading_3: RichTextToggleable._schema


class ToggleHeading3RetrieveSchema(BaseBlockRetrieveSchema,
                                   ToggleHeading3CreateSchema):
    ...


class Heading3(BaseTextBlock):
    _create_chema = Heading3CreateSchema
    _retrieve_schema = Heading3RetrieveSchema
    _rich_text_type = RichTextNonToggleable
    _schematic_name = 'heading_3'


class ToggleHeading3(Heading3):
    _create_chema = ToggleHeading3CreateSchema
    _retrieve_schema = ToggleHeading3RetrieveSchema
    _rich_text_type = RichTextToggleable
