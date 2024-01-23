from typing import Literal

from ..base import BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text_schemas import RichTextSchema
from .rich_text_block import RichTextBlock


class NumberedListCreateSchema(BaseBlockCreateSchema):
    type: Literal['numbered_list_item'] = 'numbered_list_item'
    numbered_list_item: RichTextSchema


class NumberedListRetrieveSchema(BaseBlockRetrieveSchema,
                                 NumberedListCreateSchema):
    ...


class NumberedListItem(RichTextBlock):
    _schematic_type = 'numbered_list_item'
    _create_chema = NumberedListCreateSchema
    _retrieve_schema = NumberedListRetrieveSchema
    _rich_text_schema = RichTextSchema
