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
from dataclasses import dataclass, field
from typing import Any, Iterable, List, Mapping
from dataclasses_json import LetterCase, dataclass_json, config

from card_framework import list_field
from ..widget import Widget
from .button import Button


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ButtonList(Widget):
  """ButtonList

  This will render a ButtonList widget.

  https://developers.google.com/chat/api/guides/message-formats/cards#buttonlist
  """
  buttons: List[Button] = list_field()

  @property
  def _widget_tag(self) -> str:
    """The widget tag name.

    Returns:
        str: The key by which the widget will be rendered in the Section.
    """
    return 'buttonList'

  def render(self) -> Mapping[str, Any]:
    """Renders the response to json.

    Returns:
        Mapping[str, Any]: _description_
    """
    return {self._widget_tag: self.to_dict()}
