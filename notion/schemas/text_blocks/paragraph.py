from typing import Literal

from .. import BlockCreateUpdateSchema, BlockRetrieveSchema
from .fragments import RichTextSchema


class ParagraphCreateUpdateSchema(BlockCreateUpdateSchema):
    type: Literal['paragraph'] = 'paragraph'
    paragraph: RichTextSchema


class ParagraphRetrieveSchema(BlockRetrieveSchema,
                              ParagraphCreateUpdateSchema):
    ...
