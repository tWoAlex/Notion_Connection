from typing import Literal

from .. import BlockCreateUpdateSchema, BlockRetrieveSchema
from .fragments import RichTextCheckableSchema


class ToDoCreateUpdateSchema(BlockCreateUpdateSchema):
    type: Literal['to_do'] = 'to_do'
    to_do: RichTextCheckableSchema


class ToDoRetrieveSchema(BlockRetrieveSchema,
                         ToDoCreateUpdateSchema):
    ...
