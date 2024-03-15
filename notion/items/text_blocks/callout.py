from dataclasses import dataclass

from notion.schemas.text_blocks import (CalloutCreateUpdateSchema,
                                        CalloutRetrieveSchema)

from .fragments import RichText
from . import BaseRichTextBlock


@dataclass
class Callout(BaseRichTextBlock):
    _schema_to = CalloutCreateUpdateSchema
    _schema_from = CalloutRetrieveSchema
    _rich_text_type = RichText
