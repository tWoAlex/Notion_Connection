from dataclasses import dataclass

from notion.schemas.text_blocks import (ToDoCreateUpdateSchema,
                                        ToDoRetrieveSchema)

from .fragments import RichTextCheckable
from . import BaseRichTextBlock


@dataclass
class ToDo(BaseRichTextBlock):
    _schema_to = ToDoCreateUpdateSchema
    _schema_from = ToDoRetrieveSchema
    _rich_text_type = RichTextCheckable

    checked: bool

    @property
    def checked(self) -> bool:
        return self._rich_text.checked

    @checked.setter
    def checked(self, value) -> bool:
        self._rich_text.checked = value if isinstance(value, bool) else False
