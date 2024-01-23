from typing import Any, Literal

from ..base import NotionBlock, BaseBlockCreateSchema, BaseBlockRetrieveSchema


class DividerCreateSchema(BaseBlockCreateSchema):
    type: Literal['divider'] = 'divider'
    divider: dict = dict()


class DividerRetrieveSchema(BaseBlockRetrieveSchema, DividerCreateSchema):
    ...


class Divider(NotionBlock):
    _schematic_type = 'divider'

    @classmethod
    def from_schema(cls, schema: DividerRetrieveSchema) -> Any:
        divider = Divider()
        divider.id = schema.id
        divider.parent_id = schema.parent[schema.parent['type']]
        return divider

    @classmethod
    def from_json_dict(cls, json_dict: dict[str, Any]) -> Any:
        return cls.from_schema(DividerRetrieveSchema
                               .model_validate(json_dict))

    def create_request_schema(self) -> DividerCreateSchema:
        return DividerCreateSchema()
