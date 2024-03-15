from typing import List, Literal

from pydantic import AliasChoices, BaseModel, Field

BLOCK_TYPES = ('block', 'comment',
               'database', 'page', 'page_or_database',
               'property_item', 'user')


class PaginatableResponseSchema(BaseModel):
    """ Schema for responses from
    https://developers.notion.com/reference/intro#responses"""

    # type: BLOCK_TYPES_LITERAL
    type: Literal[*BLOCK_TYPES]
    object_data: dict = Field(validation_alias=AliasChoices(*BLOCK_TYPES))

    has_more: bool = False
    next_cursor: str | None = None
    object: Literal['list']
    results: List
