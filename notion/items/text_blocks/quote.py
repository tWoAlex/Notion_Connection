from dataclasses import dataclass

from notion.schemas.text_blocks import (QuoteCreateUpdateSchema,
                                        QuoteRetrieveSchema)

from .fragments import RichText
from . import BaseRichTextBlock


@dataclass
class Quote(BaseRichTextBlock):
    _schema_to = QuoteCreateUpdateSchema
    _schema_from = QuoteRetrieveSchema
    _rich_text_type = RichText
