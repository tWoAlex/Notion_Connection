from typing import Literal

from .. import BlockCreateUpdateSchema, BlockRetrieveSchema
from .fragments import RichTextNonToggleableSchema, RichTextToggleableSchema


# Create schemas:

class Heading1CreateUpdateSchema(BlockCreateUpdateSchema):
    type: Literal['heading_1'] = 'heading_1'
    heading_1: RichTextNonToggleableSchema


class ToggleHeading1CreateUpdateSchema(Heading1CreateUpdateSchema):
    heading_1: RichTextToggleableSchema


class Heading2CreateUpdateSchema(BlockCreateUpdateSchema):
    type: Literal['heading_2'] = 'heading_2'
    heading_2: RichTextNonToggleableSchema


class ToggleHeading2CreateUpdateSchema(Heading2CreateUpdateSchema):
    heading_2: RichTextToggleableSchema


class Heading3CreateUpdateSchema(BlockCreateUpdateSchema):
    type: Literal['heading_3'] = 'heading_3'
    heading_3: RichTextNonToggleableSchema


class ToggleHeading3CreateUpdateSchema(Heading3CreateUpdateSchema):
    heading_3: RichTextToggleableSchema


#  Retrieve schemas:

class Heading1RetrieveSchema(BlockRetrieveSchema,
                             Heading1CreateUpdateSchema):
    ...


class ToggleHeading1RetrieveSchema(BlockRetrieveSchema,
                                   ToggleHeading1CreateUpdateSchema):
    ...


class Heading2RetrieveSchema(BlockRetrieveSchema,
                             Heading2CreateUpdateSchema):
    ...


class ToggleHeading2RetrieveSchema(BlockRetrieveSchema,
                                   ToggleHeading2CreateUpdateSchema):
    ...


class Heading3RetrieveSchema(BlockRetrieveSchema,
                             Heading3CreateUpdateSchema):
    ...


class ToggleHeading3RetrieveSchema(BlockRetrieveSchema,
                                   ToggleHeading3CreateUpdateSchema):
    ...
