from dataclasses import dataclass

from notion.schemas.text_blocks import (ParagraphCreateUpdateSchema,
                                        ParagraphRetrieveSchema)

from .fragments import RichText
from . import BaseRichTextBlock


@dataclass
class Paragraph(BaseRichTextBlock):
    _schema_to = ParagraphCreateUpdateSchema
    _schema_from = ParagraphRetrieveSchema
    _rich_text_type = RichText
