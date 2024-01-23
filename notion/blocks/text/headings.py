from typing import Literal

from ..base import BaseBlockCreateSchema, BaseBlockRetrieveSchema
from .fragments.rich_text_schemas import (RichTextNonToggleableSchema,
                                          RichTextToggleableSchema)
from .rich_text_block import RichTextBlock


# Create schemas:

class Heading1CreateSchema(BaseBlockCreateSchema):
    type: Literal['heading_1'] = 'heading_1'
    heading_1: RichTextNonToggleableSchema


class ToggleHeading1CreateSchema(Heading1CreateSchema):
    heading_1: RichTextToggleableSchema


class Heading2CreateSchema(BaseBlockCreateSchema):
    type: Literal['heading_2'] = 'heading_2'
    heading_2: RichTextNonToggleableSchema


class ToggleHeading2CreateSchema(Heading2CreateSchema):
    heading_2: RichTextToggleableSchema


class Heading3CreateSchema(BaseBlockCreateSchema):
    type: Literal['heading_3'] = 'heading_3'
    heading_3: RichTextNonToggleableSchema


class ToggleHeading3CreateSchema(Heading3CreateSchema):
    heading_3: RichTextToggleableSchema


#  Retrieve schemas:

class Heading1RetrieveSchema(BaseBlockRetrieveSchema,
                             Heading1CreateSchema):
    ...


class ToggleHeading1RetrieveSchema(BaseBlockRetrieveSchema,
                                   ToggleHeading1CreateSchema):
    ...


class Heading2RetrieveSchema(BaseBlockRetrieveSchema,
                             Heading2CreateSchema):
    ...


class ToggleHeading2RetrieveSchema(BaseBlockRetrieveSchema,
                                   ToggleHeading2CreateSchema):
    ...


class Heading3RetrieveSchema(BaseBlockRetrieveSchema,
                             Heading3CreateSchema):
    ...


class ToggleHeading3RetrieveSchema(BaseBlockRetrieveSchema,
                                   ToggleHeading3CreateSchema):
    ...


# Classes:

class Heading1(RichTextBlock):
    _schematic_type = 'heading_1'
    _create_chema = Heading1CreateSchema
    _retrieve_schema = Heading1RetrieveSchema
    _rich_text_schema = RichTextNonToggleableSchema


class ToggleHeading1(Heading1):
    _create_chema = ToggleHeading1CreateSchema
    _retrieve_schema = ToggleHeading1RetrieveSchema
    _rich_text_schema = RichTextToggleableSchema


class Heading2(RichTextBlock):
    _schematic_type = 'heading_2'
    _create_chema = Heading2CreateSchema
    _retrieve_schema = Heading2RetrieveSchema
    _rich_text_schema = RichTextNonToggleableSchema


class ToggleHeading2(Heading2):
    _create_chema = ToggleHeading2CreateSchema
    _retrieve_schema = ToggleHeading2RetrieveSchema
    _rich_text_schema = RichTextToggleableSchema


class Heading3(RichTextBlock):
    _schematic_type = 'heading_3'
    _create_chema = Heading3CreateSchema
    _retrieve_schema = Heading3RetrieveSchema
    _rich_text_schema = RichTextNonToggleableSchema


class ToggleHeading3(Heading3):
    _create_chema = ToggleHeading3CreateSchema
    _retrieve_schema = ToggleHeading3RetrieveSchema
    _rich_text_schema = RichTextToggleableSchema
