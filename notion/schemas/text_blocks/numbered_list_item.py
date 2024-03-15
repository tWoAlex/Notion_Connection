from typing import Literal

from .. import BlockCreateUpdateSchema, BlockRetrieveSchema
from .fragments import RichTextSchema


class NumberedListCreateUpdateSchema(BlockCreateUpdateSchema):
    type: Literal['numbered_list_item'] = 'numbered_list_item'
    numbered_list_item: RichTextSchema


class NumberedListRetrieveSchema(BlockRetrieveSchema,
                                 NumberedListCreateUpdateSchema):
    ...
