from typing import Literal

from pydantic import BaseModel

from ....core.literals import TextColor


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
