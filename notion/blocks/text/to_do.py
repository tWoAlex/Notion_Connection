from typing import Any, Literal

from ..base import BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text_schemas import RichTextSchema
from .rich_text_block import RichTextBlock
from .fragments.text_fragment import TextFragment


class RichTextCheckableSchema(RichTextSchema):
    checked: bool = False


class ToDoCreateSchema(BaseBlockCreateSchema):
    type: Literal['to_do'] = 'to_do'
    to_do: RichTextCheckableSchema


class ToDoRetrieveSchema(BaseBlockRetrieveSchema,
                         ToDoCreateSchema):
    ...


class ToDo(RichTextBlock):
    _schematic_type = 'to_do'
    _create_chema = ToDoCreateSchema
    _retrieve_schema = ToDoRetrieveSchema
    _rich_text_schema = RichTextCheckableSchema

    def __init__(self,
                 text_fragments: list[TextFragment] = None,
                 checked: bool = False) -> None:
        super().__init__(text_fragments)
        self.checked = checked

    @classmethod
    def from_schema(cls, schema: _retrieve_schema):
        return ToDo(text_fragments=[TextFragment.from_schema(fragment)
                                    for fragment in schema.to_do.rich_text],
                    checked=schema.to_do.checked)

    @classmethod
    def from_json_dict(cls, json_dict: dict[str, Any]) -> Any:
        return cls.from_schema(cls._retrieve_schema
                               .model_validate(json_dict))

    def create_request_schema(self) -> _create_chema:
        kwargs = {
            self._schematic_type: self._rich_text_schema(
                rich_text=[fragment.create_request_schema()
                           for fragment in self.text_fragments],
                checked=self.checked
            )
        }
        return self._create_chema(**kwargs)
