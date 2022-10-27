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
from typing import List, Optional

from dataclasses_json import LetterCase, dataclass_json

from card_framework import AutoNumber, enum_field, list_field, standard_field

from ..widget import Widget
from .action import Action
from .selection_item import SelectionItem


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SelectionInput(Widget):
  """SelectionInput
  """
  class SelectionInputType(AutoNumber):
    """SelectionInputType
    """
    SWITCH = 'SWITCH'
    CHECK_BOX = 'CHECK_BOX'
    RADIO_BUTTON = 'RADIO_BUTTON'
    DROPDOWN = 'DROPDOWN'

  name: str = standard_field()
  label: Optional[str] = standard_field()
  type: SelectionInputType = enum_field()
  items: List[SelectionItem] = list_field()
  on_change_action: Optional[Action] = standard_field()

  @property
  def _widget_tag(self) -> str:
    """The widget tag name.

    Returns:
        str: The key by which the widget will be rendered in the Section.
    """
    return 'selectionInput'
