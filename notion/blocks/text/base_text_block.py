from typing import Any, Literal

from ..base import NotionBlock, BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text import RichText
from .fragments.text_fragment import TextFragment


class BaseTextBlockCreateSchema(BaseBlockCreateSchema):
    type: Literal['base_text_block'] = 'base_text_block'
    base_text_block: RichText._schema


class BaseTextBlockRetrieveSchema(BaseBlockRetrieveSchema,
                                  BaseTextBlockCreateSchema):
    ...


class BaseTextBlock(NotionBlock):
    _create_chema = BaseTextBlockCreateSchema
    _retrieve_schema = BaseTextBlockRetrieveSchema
    _rich_text_type = RichText
    _schematic_name = 'base_text_block'

    def __init__(self, text_fragments: list[TextFragment] = None) -> None:
        super().__init__()
        self.text_fragments = (text_fragments
                               if text_fragments else [])

    @classmethod
    def from_schema(cls, schema: _retrieve_schema) -> Any:
        item = cls(
            text_fragments=(
                cls._rich_text_type.from_schema(
                    getattr(schema, cls._schematic_name)
                ).text_fragments
            )
        )
        item.id = schema.id
        item.parent_id = schema.parent[schema.parent['type']]
        return item

    @classmethod
    def from_json_dict(cls, json_dict: dict[str, Any]) -> Any:
        return cls.from_schema(cls._retrieve_schema
                               .model_validate(json_dict))

    def create_request_schema(self) -> _create_chema:
        kwargs = {
            self._schematic_name: self._rich_text_type(
                text_fragments=self.text_fragments
            ).create_request_schema()
        }
        return self._create_chema(**kwargs)

    def plain_text(self):
        return ''.join([fragment.text
                        for fragment in self.text_fragments])
