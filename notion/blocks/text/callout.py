from typing import Literal

from ..base import BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text_schemas import RichTextSchema
from .rich_text_block import RichTextBlock


class CalloutCreateSchema(BaseBlockCreateSchema):
    type: Literal['callout'] = 'callout'
    callout: RichTextSchema


class CalloutRetrieveSchema(BaseBlockRetrieveSchema,
                            CalloutCreateSchema):
    ...


class Callout(RichTextBlock):
    _schematic_type = 'callout'
    _create_chema = CalloutCreateSchema
    _retrieve_schema = CalloutRetrieveSchema
    _rich_text_schema = RichTextSchema
