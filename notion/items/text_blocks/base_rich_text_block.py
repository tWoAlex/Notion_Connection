from abc import ABC
from dataclasses import dataclass
from typing import Any

from notion.items import Block
from notion.schemas import BlockCreateUpdateSchema, BlockRetrieveSchema

from .fragments import TextFragment, RichText


@dataclass
class BaseRichTextBlock(Block, ABC):
    """Inheritance:
    1. Define child as `dataclass`.
    2. Redefine `_schema_to` and `_schema_from` fields.
    3. Redefine `_rich_text_type` field."""

    _schema_to = BlockCreateUpdateSchema
    _schema_from = BlockRetrieveSchema
    _rich_text_type = RichText

    fragments: list[TextFragment]

    @property
    def fragments(self) -> list[TextFragment]:
        return self._rich_text.rich_text

    @fragments.setter
    def fragments(self, value) -> None:
        if not hasattr(self, '_rich_text'):
            self._rich_text = None
        if self._rich_text is None:
            self._rich_text = self._rich_text_type()
        self._rich_text.rich_text = value

    def _fields_from_schema(self, schema: _schema_from) -> None:
        super()._fields_from_schema(schema)

    def dump_schema(self) -> _schema_to:
        return self._schema_to(**{
            self._schema_to.model_fields['type'].default:
            self._rich_text.dump_schema()
        })

    @classmethod
    def from_schema(cls, schema: _schema_from) -> Any:
        new_instance = cls(
            fragments=cls._rich_text_type.from_schema(
                getattr(schema, schema.type)
            )
        )
        new_instance._fields_from_schema(schema)
        return new_instance
