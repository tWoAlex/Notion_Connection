from dataclasses import dataclass

from notion.schemas.text_blocks import (BulletedListCreateUpdateSchema,
                                        BulletedListRetrieveSchema)

from .fragments import RichText
from . import BaseRichTextBlock


@dataclass
class BulletedListItem(BaseRichTextBlock):
    _schema_to = BulletedListCreateUpdateSchema
    _schema_from = BulletedListRetrieveSchema
    _rich_text_type = RichText
