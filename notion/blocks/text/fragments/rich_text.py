from typing import Literal

from pydantic import BaseModel

from ...base import NotionFragmentBlock
from .text_color import TextColor
from .text_fragment import TextFragmentSchema, TextFragment


class RichTextSchema(BaseModel):
    color: TextColor = TextColor.DEFAULT
    rich_text: list[TextFragmentSchema]


class RichTextToggleableSchema(RichTextSchema):
    is_toggleable: Literal[True] = True


class RichTextNonToggleableSchema(RichTextSchema):
    is_toggleable: Literal[False] = False


class RichText(NotionFragmentBlock):
    _schema = RichTextSchema

    def __init__(self, text_fragments: list[TextFragment] = None) -> None:
        self.text_fragments = (text_fragments
                               if text_fragments else [])

    @classmethod
    def from_schema(cls, schema: _schema):
        return RichText(text_fragments=[TextFragment.from_schema(fragment)
                                        for fragment in schema.rich_text])

    def create_request_schema(self) -> _schema:
        return self._schema(rich_text=[fragment.create_request_schema()
                                       for fragment in self.text_fragments])


class RichTextToggleable(RichText):
    _schema = RichTextToggleableSchema


class RichTextNonToggleable(RichText):
    _schema = RichTextNonToggleableSchema
