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
from dataclasses import dataclass
from typing import List

from card_framework import list_field, enum_field, standard_field, AutoNumber
from dataclasses_json import LetterCase, dataclass_json

from ..widget import Widget
from .icon import Icon
from .on_click import OnClick


@dataclass_json
@dataclass
class Chip(Widget):
  """Chip

  Renders a Chip.

  https://developers.google.com/workspace/chat/api/reference/rest/v1/cards#chip
  """
  __SUPPRESS_TAG__ = True
  icon: Icon = standard_field()
  label: str = standard_field()
  on_click: OnClick = standard_field()
  # WARNING: `enabled` is deprecated. Use `disabled` instead
  enabled: bool = standard_field()
  disabled: bool = standard_field()
  alt_text: str = standard_field()


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ChipList(Widget):
  """ChipList

  This will render a ChipList widget.

  https://developers.google.com/chat/api/guides/message-formats/cards#chiplist
  """
  class Layout(AutoNumber):
    LAYOUT_UNSPECIFIED = ()
    WRAPPED = ()
    HORIZONTAL_SCROLLABLE = ()

  layout: Layout = enum_field()
  chips: List[Chip] = list_field()
