from typing import Any, Literal

from ..base import NotionBlock
from ..base import BaseBlockCreate, BaseBlockRetrieve
from . import TextColor
from .rich_text import RichTextSchema, RichText
from .text_fragment import TextFragment


class ParagraphCreateSchema(BaseBlockCreate):
    type: Literal['paragraph'] = 'paragraph'
    paragraph: RichTextSchema


class ParagraphRetrieveSchema(BaseBlockRetrieve, ParagraphCreateSchema):
    ...


class Paragraph(NotionBlock):
    def __init__(self, text_fragments: list[TextFragment] = None) -> None:
        self.text_fragments = (text_fragments
                               if text_fragments else [])

    def create_request_schema(self) -> ParagraphCreateSchema:
        return ParagraphCreateSchema(
            paragraph=RichText(
                common_color=TextColor.DEFAULT,
                text_fragments=self.text_fragments
            ).create_request_schema()
        )

    @classmethod
    def from_schema(cls, schema: ParagraphRetrieveSchema) -> Any:
        paragraph = cls(text_fragments=(
            RichText.from_schema(schema.paragraph).text_fragments))
        paragraph.id = schema.id
        return paragraph

    @classmethod
    def from_json_dict(cls, json_dict: dict[str, Any]) -> Any:
        schema = ParagraphRetrieveSchema.model_validate(json_dict)
        return cls.from_schema(schema)
