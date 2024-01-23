from typing import Literal

from ..base import BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text_schemas import RichTextSchema
from .rich_text_block import RichTextBlock


class ToggleCreateSchema(BaseBlockCreateSchema):
    type: Literal['toggle'] = 'toggle'
    toggle: RichTextSchema


class ToggleRetrieveSchema(BaseBlockRetrieveSchema,
                           ToggleCreateSchema):
    ...


class Toggle(RichTextBlock):
    _schematic_type = 'toggle'
    _create_chema = ToggleCreateSchema
    _retrieve_schema = ToggleRetrieveSchema
    _rich_text_schema = RichTextSchema
