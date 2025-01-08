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
from typing import Dict, List, Optional

import dataclasses_json
from card_framework import standard_field

from .action import Action
from .icon import Icon
from .open_link import OpenLink
from ..widget import Widget

@dataclasses_json.dataclass_json
@dataclasses.dataclass
class OverflowMenuItem(object):
  start_icon: Optional[Icon] = standard_field()
  text: Optional[str] = standard_field()
  # Should be an OnClick, but it can't be done because of a circular
  # import (OnClick -> OverflowMenu -> OverflowMenuItem -> OnClick)
  on_click: Optional[Widget] = standard_field()
  disabled: Optional[bool] = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class OverflowMenu(object):
  items: List[OverflowMenuItem] = standard_field()
