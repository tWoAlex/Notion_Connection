from .divider import Divider # noqa
from .fragments import TextColor, TextFragment # noqa
from .paragraph import Paragraph # noqa
from .headings import (Heading1, ToggleHeading1, # noqa
                       Heading2, ToggleHeading2, # noqa
                       Heading3, ToggleHeading3,) # noqa
from .toggle import Toggle # noqa
from .to_do import ToDo # noqa
from .bulleted_list_item import BulletedListItem # noqa
from .numbered_list_item import NumberedListItem # noqa


block_types = (Divider, Paragraph,
               Heading1, ToggleHeading1,
               Heading2, ToggleHeading2,
               Heading3, ToggleHeading3,
               Toggle, ToDo,
               BulletedListItem, NumberedListItem)

text_types = (Paragraph,
              Heading1, ToggleHeading1,
              Heading2, ToggleHeading2,
              Heading3, ToggleHeading3,
              Toggle, ToDo,
              BulletedListItem, NumberedListItem)
