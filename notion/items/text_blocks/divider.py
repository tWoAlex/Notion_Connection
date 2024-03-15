from dataclasses import dataclass
from typing import Any

from notion.items import Block
from notion.schemas.text_blocks import (DividerCreateSchema,
                                        DividerRetrieveSchema)


@dataclass
class Divider(Block):
    _schema_to = DividerCreateSchema
    _schema_from = DividerRetrieveSchema

    def _fields_from_schema(self, schema: _schema_from) -> None:
        super()._fields_from_schema(schema)

    def dump_schema(self) -> _schema_to:
        return self._schema_to()

    @classmethod
    def from_schema(cls, schema: _schema_from) -> Any:
        new_instance = cls()
        new_instance._fields_from_schema(schema)
        return new_instance
