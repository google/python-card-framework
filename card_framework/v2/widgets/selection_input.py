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
from typing import Any, Dict, List, Optional

from dataclasses_json import (LetterCase, config,
                              dataclass_json)
from dataclasses_json.core import Json

from ..enums import SelectionInputType
from ..widget import Widget
from .action import Action
from .selection_item import SelectionItem


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SelectionInput(Widget):
  """SelectionInput
  """
  name: str = ''
  label: Optional[str] = None
  type: SelectionInputType = field(
      default=None,
      metadata=config(exclude=lambda x: not x,
                      encoder=lambda x: x.name if x else None))
  items: List[SelectionItem] = field(
      default_factory=list, metadata=config(exclude=lambda x: not x))
  on_change_action: Optional[Action] = None

  @property
  def _widget_tag(self) -> str:
    """The widget tag name.

    Returns:
        str: The key by which the widget will be rendered in the Section.
    """
    return 'selectionInput'
