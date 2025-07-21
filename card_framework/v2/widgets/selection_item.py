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

from card_framework import Renderable, list_field, standard_field


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class SelectionItem(Renderable):
  __SUPPRESS_TAG__ = True

  text: str = standard_field()
  value: str = standard_field()
  selected: bool = standard_field()
  start_icon_uri: str = standard_field()
  bottom_text: str = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class SelectionItems(Renderable):
  __SUPPRESS_TAG__ = True

  items: List[SelectionItem] = list_field()
