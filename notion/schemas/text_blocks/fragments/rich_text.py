from typing import Literal

from pydantic import BaseModel

from ....core.literals import TextColor
from . import TextFragmentSchema


class RichTextSchema(BaseModel):
    color: TextColor = TextColor.DEFAULT
    rich_text: list[TextFragmentSchema]


class RichTextToggleableSchema(RichTextSchema):
    is_toggleable: Literal[True] = True


class RichTextNonToggleableSchema(RichTextSchema):
    is_toggleable: Literal[False] = False


class RichTextCheckableSchema(RichTextSchema):
    checked: bool = False
