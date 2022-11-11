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
import dataclasses
from typing import List, Optional

import dataclasses_json
from card_framework import AutoNumber, enum_field, list_field, standard_field

from ..widget import Widget
from .action import Action
from .selection_item import SelectionItem


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class SelectionInput(Widget):
  """SelectionInput
  """
  class SelectionType(AutoNumber):
    """SelectionType
    """
    SWITCH = ()
    CHECK_BOX = ()
    RADIO_BUTTON = ()
    DROPDOWN = ()

  name: str = standard_field()
  label: Optional[str] = standard_field()
  type: SelectionType = enum_field()
  items: List[SelectionItem] = list_field()
  on_change_action: Optional[Action] = standard_field()
