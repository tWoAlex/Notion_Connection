from typing import Any
from pydantic import BaseModel, ValidationError

from ..base import NotionFragmentBlock
from . import TextColor
from .text_fragment import TextFragment, TextFragmentSchema


# Schemas
class RichTextSchema(BaseModel):
    color: TextColor = TextColor.DEFAULT
    rich_text: list[TextFragmentSchema]


# class RichTextToggleableSchema(RichTextSchema):
#     is_toggleable: bool = True


# class RichTextNonToggleableSchema(RichTextSchema):
#     is_toggleable: bool = False


# Class
class RichText(NotionFragmentBlock):
    def __init__(self, common_color: TextColor = TextColor.DEFAULT,
                 text_fragments: list[TextFragment] = None) -> None:
        self.color = common_color
        self.text_fragments = (text_fragments
                               if text_fragments else [])

    def create_request_schema(self) -> RichTextSchema:
        return RichTextSchema(color=self.color,
                              rich_text=[fragment.create_request_schema()
                                         for fragment in self.text_fragments])

    @classmethod
    def from_schema(cls, schema: RichTextSchema):
        return cls(common_color=schema.color,
                   text_fragments=[
                       TextFragment.from_schema(fragment)
                       for fragment in schema.rich_text])
