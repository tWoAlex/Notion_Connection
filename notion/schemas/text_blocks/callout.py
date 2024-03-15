from typing import Literal

from .. import BlockCreateUpdateSchema, BlockRetrieveSchema
from .fragments import RichTextSchema


class CalloutCreateUpdateSchema(BlockCreateUpdateSchema):
    type: Literal['callout'] = 'callout'
    callout: RichTextSchema


class CalloutRetrieveSchema(BlockRetrieveSchema,
                            CalloutCreateUpdateSchema):
    ...
