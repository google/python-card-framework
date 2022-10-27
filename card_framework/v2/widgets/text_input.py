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
from typing import Optional

from card_framework import AutoNumber, enum_field, standard_field
from dataclasses_json import LetterCase, dataclass_json

from ..widget import Widget
from .action import Action
from .suggestions import Suggestions


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TextInput(Widget):
  """TextInput
  """
  class Type(AutoNumber):
    """TextInputType
    """
    SINGLE_LINE = 'SINGLE_LINE'
    MULTIPLE_LINE = 'MULTIPLE_LINE'

  name: str = standard_field()
  label: Optional[str] = standard_field()
  hint_text: Optional[str] = standard_field()
  value: Optional[str] = standard_field()
  type: Type = enum_field()
  on_change_action: Optional[Action] = standard_field()
  initial_suggestions: Optional[Suggestions] = standard_field()
  auto_complete_action: Optional[Action] = standard_field()

  @property
  def _widget_tag(self) -> str:
    """The widget tag name.

    Returns:
        str: The key by which the widget will be rendered in the Section.
    """
    return 'textInput'
