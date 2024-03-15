from dataclasses import dataclass

from notion.schemas.text_blocks import (NumberedListCreateUpdateSchema,
                                        NumberedListRetrieveSchema)

from .fragments import RichText
from . import BaseRichTextBlock


@dataclass
class NumberedListItem(BaseRichTextBlock):
    _schema_to = NumberedListCreateUpdateSchema
    _schema_from = NumberedListRetrieveSchema
    _rich_text_type = RichText
