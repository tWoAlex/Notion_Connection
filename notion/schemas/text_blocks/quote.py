from typing import Literal

from .. import BlockCreateUpdateSchema, BlockRetrieveSchema
from .fragments import RichTextSchema


class QuoteCreateUpdateSchema(BlockCreateUpdateSchema):
    type: Literal['quote'] = 'quote'
    quote: RichTextSchema


class QuoteRetrieveSchema(BlockRetrieveSchema,
                          QuoteCreateUpdateSchema):
    ...
