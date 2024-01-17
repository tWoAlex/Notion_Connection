from enum import Enum

from pydantic import BaseModel


class TextColor(str, Enum):
    DEFAULT = 'default'

    BLUE = 'blue'
    BLUE_BACKGROUND = 'blue_background'
    BROWN = 'brown'
    BROWN_BACKGROUND = 'brown_background'
    GRAY = 'gray'
    GRAY_BACKGROUND = 'gray_background'
    GREEN = 'green'
    GREEN_BACKGROUND = 'green_background'
    ORANGE = 'orange'
    ORANGE_BACKGROUND = 'orange_background'
    PINK = 'pink'
    PINK_BACKGROUND = 'pink_background'
    PURPLE = 'purple'
    PURPLE_BACKGROUND = 'purple_background'
    RED = 'red'
    RED_BACKGROUND = 'red_background'
    YELLOW = 'yellow'
    YELLOW_BACKGROUND = 'yellow_background'


class AnnotationsSchema(BaseModel):
    bold: bool = False
    code: bool = False
    color: TextColor = TextColor.DEFAULT
    italic: bool = False
    strikethrough: bool = False
    underline: bool = False


class UrlSchema(BaseModel):
    url: str


class TextContentSchema(BaseModel):
    content: str
    link: UrlSchema | None
