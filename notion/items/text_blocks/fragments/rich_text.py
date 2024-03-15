from dataclasses import dataclass

from . import TextFragment
from notion.schemas.text_blocks.fragments import (RichTextCheckableSchema,
                                                  RichTextNonToggleableSchema,
                                                  RichTextToggleableSchema,
                                                  RichTextSchema)


@dataclass
class RichText:
    _schema = RichTextSchema

    rich_text: list[TextFragment] = None

    def dump_schema(self) -> _schema:
        return self._schema(rich_text=[
            fragment.dump_schema()
            for fragment in self.rich_text
        ])

    @classmethod
    def from_schema(cls, schema: _schema):
        return cls(rich_text=[
            TextFragment.from_schema(schema)
            for schema in schema.rich_text
        ])


@dataclass
class RichTextNonToggleable(RichText):
    _schema = RichTextNonToggleableSchema


@dataclass
class RichTextToggleable(RichText):
    _schema = RichTextToggleableSchema


@dataclass
class RichTextCheckable(RichText):
    _schema = RichTextCheckableSchema

    checked: bool = False

    def dump_schema(self) -> _schema:
        schema = super().dump_schema()
        schema.checked = self.checked
        return schema

    @classmethod
    def from_schema(cls, schema: _schema):
        new_instance = cls(rich_text=[
            TextFragment.from_schema(schema)
            for schema in schema.rich_text
        ])
        new_instance.checked = schema.checked
        return new_instance
