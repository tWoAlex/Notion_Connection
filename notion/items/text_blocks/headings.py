from dataclasses import dataclass

from notion.schemas.text_blocks import (
    Heading1CreateUpdateSchema, Heading1RetrieveSchema,
    Heading2CreateUpdateSchema, Heading2RetrieveSchema,
    Heading3CreateUpdateSchema, Heading3RetrieveSchema,
    ToggleHeading1CreateUpdateSchema, ToggleHeading1RetrieveSchema,
    ToggleHeading2CreateUpdateSchema, ToggleHeading2RetrieveSchema,
    ToggleHeading3CreateUpdateSchema, ToggleHeading3RetrieveSchema
)

from .fragments import RichTextNonToggleable, RichTextToggleable
from . import BaseRichTextBlock


# Default headings:

@dataclass
class Heading1(BaseRichTextBlock):
    _schema_to = Heading1CreateUpdateSchema
    _schema_from = Heading1RetrieveSchema
    _rich_text_type = RichTextNonToggleable


@dataclass
class Heading2(BaseRichTextBlock):
    _schema_to = Heading2CreateUpdateSchema
    _schema_from = Heading2RetrieveSchema
    _rich_text_type = RichTextNonToggleable


@dataclass
class Heading3(BaseRichTextBlock):
    _schema_to = Heading3CreateUpdateSchema
    _schema_from = Heading3RetrieveSchema
    _rich_text_type = RichTextNonToggleable


# Toggleable headings:

@dataclass
class ToggleHeading1(BaseRichTextBlock):
    _schema_to = ToggleHeading1CreateUpdateSchema
    _schema_from = ToggleHeading1RetrieveSchema
    _rich_text_type = RichTextToggleable


@dataclass
class ToggleHeading2(BaseRichTextBlock):
    _schema_to = ToggleHeading2CreateUpdateSchema
    _schema_from = ToggleHeading2RetrieveSchema
    _rich_text_type = RichTextToggleable


@dataclass
class ToggleHeading3(BaseRichTextBlock):
    _schema_to = ToggleHeading3CreateUpdateSchema
    _schema_from = ToggleHeading3RetrieveSchema
    _rich_text_type = RichTextToggleable
