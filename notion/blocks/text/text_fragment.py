from typing import Any, Literal

from pydantic import BaseModel, ValidationError

from ..base import NotionFragmentBlock
from . import TextColor


# Schemas

class AnnotationsSchema(BaseModel):
    bold: bool = False
    code: bool = False
    color: TextColor = TextColor.DEFAULT
    italic: bool = False
    strikethrough: bool = False
    underline: bool = False


class UrlSchema(BaseModel):
    url: str


class TextContentSchema(BaseModel):
    content: str
    link: UrlSchema | None


class TextFragmentSchema(BaseModel):
    annotations: AnnotationsSchema = AnnotationsSchema()
    href: str | None = None
    plain_text: str
    text: TextContentSchema
    type: Literal['text'] = 'text'


# Classes
class TextFragment(NotionFragmentBlock):
    def __init__(self, text: str = '', link: str = None,
                 color: TextColor = TextColor.DEFAULT,
                 bold: bool = False, code: bool = False,
                 italic: bool = False, strikethrough: bool = False,
                 underline: bool = False) -> None:
        self.text = text
        self.link = link
        self.color = color

        self.bold = bold
        self.code = code
        self.italic = italic
        self.strikethrough = strikethrough
        self.underline = underline

    def create_request_schema(self) -> TextFragmentSchema:
        return TextFragmentSchema(
            plain_text=self.text, href=self.link,
            annotations=AnnotationsSchema(bold=self.bold,
                                          code=self.code,
                                          color=self.color,
                                          italic=self.italic,
                                          strikethrough=self.strikethrough,
                                          underline=self.underline),
            text=TextContentSchema(content=self.text,
                                   link=(UrlSchema(url=self.link)
                                         if self.link else None))
        )

    @classmethod
    def from_schema(cls, schema: TextFragmentSchema) -> Any:
        annotations = schema.annotations
        return cls(text=schema.text.content,
                   link=(schema.text.link.url
                         if schema.text.link else None),
                   color=annotations.color,
                   bold=annotations.bold,
                   code=annotations.code,
                   italic=annotations.italic,
                   strikethrough=annotations.strikethrough,
                   underline=annotations.underline)
