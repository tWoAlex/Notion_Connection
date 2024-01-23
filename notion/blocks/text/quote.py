from typing import Literal

from ..base import BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text_schemas import RichTextSchema
from .rich_text_block import RichTextBlock


class QuoteCreateSchema(BaseBlockCreateSchema):
    type: Literal['quote'] = 'quote'
    quote: RichTextSchema


class QuoteRetrieveSchema(BaseBlockRetrieveSchema,
                          QuoteCreateSchema):
    ...


class Quote(RichTextBlock):
    _schematic_type = 'quote'
    _create_chema = QuoteCreateSchema
    _retrieve_schema = QuoteRetrieveSchema
    _rich_text_schema = RichTextSchema
