from typing import Literal

from ..base import BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text import RichText
from .base_text_block import BaseTextBlock


class ParagraphCreateSchema(BaseBlockCreateSchema):
    type: Literal['paragraph'] = 'paragraph'
    paragraph: RichText._schema


class ParagraphRetrieveSchema(BaseBlockRetrieveSchema,
                              ParagraphCreateSchema):
    ...


class Paragraph(BaseTextBlock):
    _create_chema = ParagraphCreateSchema
    _retrieve_schema = ParagraphRetrieveSchema
    _rich_text_type = RichText
    _schematic_name = 'paragraph'
