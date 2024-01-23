from typing import Literal

from ..base import BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text_schemas import RichTextSchema
from .rich_text_block import RichTextBlock


class ParagraphCreateSchema(BaseBlockCreateSchema):
    type: Literal['paragraph'] = 'paragraph'
    paragraph: RichTextSchema


class ParagraphRetrieveSchema(BaseBlockRetrieveSchema,
                              ParagraphCreateSchema):
    ...


class Paragraph(RichTextBlock):
    _schematic_type = 'paragraph'
    _create_chema = ParagraphCreateSchema
    _retrieve_schema = ParagraphRetrieveSchema
    _rich_text_schema = RichTextSchema
