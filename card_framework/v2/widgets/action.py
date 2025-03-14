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

from dataclasses import dataclass
from typing import List, Optional

from card_framework import AutoNumber, enum_field, list_field, standard_field
from dataclasses_json import dataclass_json

from ..widget import Widget


@dataclass_json
@dataclass
class Action(Widget):
  class Interaction(AutoNumber):
    UNSPECIFIED = ()
    OPEN_DIALOG = ()

  class LoadIndicator(AutoNumber):
    """LoadIndicator
    """
    SPINNER = ()
    NONE = ()

  function: str = standard_field(default='')
  parameters: List[ActionParameter] = list_field()
  load_indicator: LoadIndicator = enum_field()
  persist_values: bool = standard_field()
  interaction: Optional[Interaction] = enum_field()
  required_widgets: Optional[List[str]] = list_field()
  all_widgets_are_required: Optional[bool] = standard_field()


@dataclass_json
@dataclass
class ActionParameter(object):
  key: str = standard_field()
  value: str = standard_field()
