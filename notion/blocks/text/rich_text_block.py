from typing import Any, Literal

from ..base import NotionBlock, BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text_schemas import RichTextSchema
from .fragments.text_fragment import TextFragment


class RichTextBlockCreateSchema(BaseBlockCreateSchema):
    """Override:
    type: Literal['{{ json_type_name }}] = '{{ json_type_name }}'
    {{ json_type_name }}: RichTextSchema or its child"""

    type: Literal['base_text_block'] = 'base_text_block'
    base_text_block: RichTextSchema


class RichTextBlockRetrieveSchema(BaseBlockRetrieveSchema,
                                  RichTextBlockCreateSchema):
    ...


class RichTextBlock(NotionBlock):
    """Override:
    _schematic_type = '{{ json_type_name }}'
    _create_chema = RichTextBlockCreateSchema or its child
    _retrieve_schema = RichTextBlockRetrieveSchema or its child
    _rich_text_schema = RichTextSchema or its child
    """

    _schematic_type = 'base_text_block'
    _create_chema = RichTextBlockCreateSchema
    _retrieve_schema = RichTextBlockRetrieveSchema
    _rich_text_schema = RichTextSchema

    def __init__(self, text_fragments: list[TextFragment]) -> None:
        super().__init__()
        self.text_fragments = (text_fragments
                               if text_fragments else [])

    @classmethod
    def from_schema(cls, schema: _retrieve_schema) -> Any:
        item = cls(
            text_fragments=[
                TextFragment.from_schema(fragment)
                for fragment in getattr(schema, cls._schematic_type).rich_text
            ]
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
            self._schematic_type: self._rich_text_schema(
                rich_text=[fragment.create_request_schema()
                           for fragment in self.text_fragments]
            )
        }
        return self._create_chema(**kwargs)

    def plain_text(self):
        return ''.join([fragment.text
                        for fragment in self.text_fragments])
