from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class BlockCreateUpdateSchema(BaseModel):
    object: Literal['block'] = 'block'


class BlockRetrieveSchema(BlockCreateUpdateSchema):
    id: str = None
    parent: dict[str, str]

    created_time: datetime
    last_edited_time: datetime
