from typing import Literal

from ..base import BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text_schemas import RichTextSchema
from .rich_text_block import RichTextBlock


class BulletedListCreateSchema(BaseBlockCreateSchema):
    type: Literal['bulleted_list_item'] = 'bulleted_list_item'
    bulleted_list_item: RichTextSchema


class BulletedListRetrieveSchema(BaseBlockRetrieveSchema,
                                 BulletedListCreateSchema):
    ...


class BulletedListItem(RichTextBlock):
    _schematic_type = 'bulleted_list_item'
    _create_chema = BulletedListCreateSchema
    _retrieve_schema = BulletedListRetrieveSchema
    _rich_text_schema = RichTextSchema
