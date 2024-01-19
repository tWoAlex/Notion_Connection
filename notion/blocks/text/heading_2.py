from typing import Literal

from ..base import BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text import RichTextNonToggleable, RichTextToggleable
from .base_text_block import BaseTextBlock


class Heading2CreateSchema(BaseBlockCreateSchema):
    type: Literal['heading_2'] = 'heading_2'
    heading_2: RichTextNonToggleable._schema


class Heading2RetrieveSchema(BaseBlockRetrieveSchema,
                             Heading2CreateSchema):
    ...


class ToggleHeading2CreateSchema(Heading2CreateSchema):
    heading_2: RichTextToggleable._schema


class ToggleHeading2RetrieveSchema(BaseBlockRetrieveSchema,
                                   ToggleHeading2CreateSchema):
    ...


class Heading2(BaseTextBlock):
    _create_chema = Heading2CreateSchema
    _retrieve_schema = Heading2RetrieveSchema
    _rich_text_type = RichTextNonToggleable
    _schematic_name = 'heading_2'


class ToggleHeading2(Heading2):
    _create_chema = ToggleHeading2CreateSchema
    _retrieve_schema = ToggleHeading2RetrieveSchema
    _rich_text_type = RichTextToggleable
