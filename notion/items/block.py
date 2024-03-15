import abc
from datetime import datetime
from typing import Any

from notion.schemas import BlockCreateUpdateSchema, BlockRetrieveSchema


class Block(abc.ABC):
    """Inheritance:
    1. Define child as `dataclass`.
    2. Redefine `_schema_to` and `_schema_from` fields.
    3. If needed, redefine `_fields_from_schema` method,
    including `super()._fields_from_schema`.
    4. Redefine `dump_schema` medthod and `from_schema` classmethod."""

    _schema_to = BlockCreateUpdateSchema
    _schema_from = BlockRetrieveSchema

    id: str = None
    parent_id: str = None
    created_time: datetime = None
    last_edited_time: datetime = None

    def _fields_from_schema(self, schema: _schema_from) -> None:
        """Sets instance fields from given schema"""
        for field in ('id', 'created_time', 'last_edited_time'):
            setattr(self, field, getattr(schema, field))
        self.parent_id = schema.parent[schema.parent['type']]

    @abc.abstractmethod
    def dump_schema(self) -> _schema_to:
        """Dumps instance to schema instance"""
        ...

    def dump_json_dict(self) -> dict:
        """Dumps instance to dict"""
        return self.dump_schema().model_dump()

    @abc.abstractclassmethod
    def from_schema(cls, schema: _schema_from) -> Any:
        """Creates instance from schema instance"""
        ...

    @classmethod
    def from_json_dict(cls, data: dict) -> Any:
        """Creates instance from json dict"""
        return cls.from_schema(cls._schema_from.model_validate(data))
