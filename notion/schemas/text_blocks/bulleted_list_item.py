from typing import Literal

from .. import BlockCreateUpdateSchema, BlockRetrieveSchema
from .fragments import RichTextSchema


class BulletedListCreateUpdateSchema(BlockCreateUpdateSchema):
    type: Literal['bulleted_list_item'] = 'bulleted_list_item'
    bulleted_list_item: RichTextSchema


class BulletedListRetrieveSchema(BlockRetrieveSchema,
                                 BulletedListCreateUpdateSchema):
    ...
