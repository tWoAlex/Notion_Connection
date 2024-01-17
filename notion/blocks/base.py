import abc
import json
from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel


# Schemas

class BaseBlockCreate(BaseModel):
    object: Literal['block'] = 'block'


class BaseBlockRetrieve(BaseModel):
    archived: bool = False
    id: str = None
    parent: dict
    has_children: bool = False

    created_time: datetime
    last_edited_time: datetime
    created_by: dict
    last_edited_by: dict


# Classes

class NotionFragmentBlock(abc.ABC):
    @abc.abstractmethod
    def create_request_schema(self) -> Any:
        ...

    @abc.abstractclassmethod
    def from_schema(cls, schema) -> Any:
        ...


class NotionBlock(NotionFragmentBlock):
    @abc.abstractclassmethod
    def from_json_dict(cls, json_dict: dict[str, Any]) -> Any:
        ...

    @classmethod
    def from_json_str(cls, json_str: str) -> Any:
        return cls.from_json_dict(json.loads(json_str))
