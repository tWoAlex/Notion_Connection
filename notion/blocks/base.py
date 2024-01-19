import abc
import json
from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel


class BaseBlockCreateSchema(BaseModel):
    object: Literal['block'] = 'block'


class BaseBlockRetrieveSchema(BaseBlockCreateSchema):
    id: str = None
    parent: dict[str, str]

    created_time: datetime
    created_by: dict
    last_edited_time: datetime
    last_edited_by: dict


class NotionFragmentBlock(abc.ABC):
    @abc.abstractclassmethod
    def from_schema(cls, schema) -> Any:
        ...

    @abc.abstractmethod
    def create_request_schema(self) -> Any:
        ...

    def create_request_json(self) -> Any:
        return self.create_request_schema().model_dump()


class NotionBlock(NotionFragmentBlock):
    def __init__(self) -> None:
        self.id = None
        self.parent_id = None

        self.created_time = None
        self.created_by = None
        self.last_edited_time = None
        self.last_edited_by = None

    @abc.abstractclassmethod
    def from_json_dict(cls, json_dict: dict[str, Any]) -> Any:
        ...

    @classmethod
    def from_json_str(cls, json_str: str) -> Any:
        return cls.from_json_dict(json.loads(json_str))
