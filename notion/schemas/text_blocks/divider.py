from typing import Literal

from .. import BlockCreateUpdateSchema, BlockRetrieveSchema


class DividerCreateSchema(BlockCreateUpdateSchema):
    type: Literal['divider'] = 'divider'
    divider: dict = dict()


class DividerRetrieveSchema(BlockRetrieveSchema, DividerCreateSchema):
    ...
