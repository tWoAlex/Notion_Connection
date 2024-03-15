from typing import Literal

from .. import BlockCreateUpdateSchema, BlockRetrieveSchema
from .fragments import RichTextSchema


class ToggleCreateUpdateSchema(BlockCreateUpdateSchema):
    type: Literal['toggle'] = 'toggle'
    toggle: RichTextSchema


class ToggleRetrieveSchema(BlockRetrieveSchema,
                           ToggleCreateUpdateSchema):
    ...
