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

import dataclasses
from typing import Any, Dict, List, Mapping, Optional

import dataclasses_json
from dataclasses_json import core

from card_framework import AutoNumber, enum_field, list_field, standard_field

from ..widget import Widget
from .action import Action
from .selection_item import SelectionItem, SelectionItems


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
  multi_select_max_selected_items: int = standard_field()
  multi_select_min_query_length: int = standard_field()
  external_data_source: Action = standard_field()
  platform_data_source: PlatformDataSource = standard_field()

  def to_dict(self, encode_json=False) -> Dict[str, core.Json]:
    self.items = self.items.items if self.items else None

    return super().to_dict(encode_json)

  def render(self) -> Mapping[str, Any]:
    return super().render()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class UpdatedWidget(Widget):
  widget: str = standard_field()
  suggestions: SelectionItems = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class PlatformDataSource(object):
  class CommonDataSource(AutoNumber):
    UNKNOWN = ()
    USER = ()

  common_data_source: CommonDataSource = enum_field()
  host_app_data_source: HostAppDataSourceMarkup = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class HostAppDataSourceMarkup(object):
  chat_data_source: ChatClientDataSourceMarkup = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ChatClientDataSourceMarkup(object):
  space_data_source: SpaceDataSource = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class SpaceDataSource(object):
  default_to_current_space: bool = standard_field(default=False)
  []
