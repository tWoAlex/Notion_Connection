from dataclasses import dataclass

from ....core.literals import TextColor
from ....schemas.text_blocks.fragments.text_fragment import (
    TextFragmentSchema, AnnotationsSchema, TextContentSchema, UrlSchema
)


@dataclass
class TextFragment:
    text: str = None
    url: str = None

    bold: bool = False
    code: bool = False
    color: TextColor = TextColor.DEFAULT
    italic: bool = False
    strikethrough: bool = False
    underline: bool = False

    _annotation_fields = (
        'bold', 'code', 'color', 'italic', 'strikethrough', 'underline'
    )

    def dump_schema(self):
        annotations = {
            field: getattr(self, field)
            for field in self._annotation_fields
        }
        return TextFragmentSchema(
            annotations=AnnotationsSchema(**annotations),
            href=self.url, plain_text=self.text,
            text=TextContentSchema(content=self.text,
                                   link=(UrlSchema(url=self.url)
                                         if self.url else None)),
        )

    @classmethod
    def from_schema(cls, data: TextFragmentSchema):
        annotations = {
            field: getattr(data.annotations, field)
            for field in cls._annotation_fields
        }
        return cls(
            **(
                {'text': data.plain_text, 'url': data.href}
                or annotations
            )
        )
