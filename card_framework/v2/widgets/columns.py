# Copyright 2022 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations

from ctypes import Union
from dataclasses import dataclass
from typing import List, Optional

from dataclasses_json import dataclass_json

from card_framework import AutoNumber, enum_field, list_field
from card_framework.v2.enums import ImageType

from ..widget import Widget
from .button_list import ButtonList
from .date_time_picker import DateTimePicker
from .decorated_text import DecoratedText
from .selection_input import SelectionInput
from .text_input import TextInput
from .text_paragraph import TextParagraph


@dataclass_json
@dataclass
class Columns(Widget):
  column_items: List[Column] = list_field()


@dataclass_json
@dataclass
class Column(object):
  __SUPPRESS_TAG__ = True

  class HorizontalSizeStyle(AutoNumber):
    HORIZONTAL_SIZE_STYLE_UNSPECIFIED = ()
    FILL_AVAILABLE_SPACE = ()
    FILL_MINIMUM_SPACE = ()

  class HorizontalAlignment(AutoNumber):
    HORIZONTAL_ALIGNMENT_UNSPECIFIED = ()
    START = ()
    CENTER = ()
    END = ()

  class VerticalAlignment(AutoNumber):
    VERTICAL_ALIGNMENT_UNSPECIFIED = ()
    CENTER = ()
    TOP = ()
    BOTTOM = ()

  horizontal_size_style: Optional[Column.HorizontalSizeStyle] = enum_field()
  horizontal_alignment: Optional[Column.HorizontalAlignment] = enum_field()
  vertical_alignment: Optional[Column.VerticalAlignment] = enum_field()
  widgets: Widget = list_field()
