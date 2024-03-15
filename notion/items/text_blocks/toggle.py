from dataclasses import dataclass

from notion.schemas.text_blocks import (ToggleCreateUpdateSchema,
                                        ToggleRetrieveSchema)

from .fragments import RichText
from . import BaseRichTextBlock


@dataclass
class Toggle(BaseRichTextBlock):
    _schema_to = ToggleCreateUpdateSchema
    _schema_from = ToggleRetrieveSchema
    _rich_text_type = RichText
