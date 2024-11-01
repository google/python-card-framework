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
from typing import Optional

from dataclasses_json import dataclass_json

from card_framework import AutoNumber, enum_field, standard_field

from ..widget import Widget
from .action import Action


@dataclass_json
@dataclass
class DateTimePicker(Widget):
  class Type(AutoNumber):
    DATE_AND_TIME = ()
    DATE_ONLY = ()
    TIME_ONLY = ()

  name: str = standard_field()
  label: Optional[str] = standard_field()
  type_: DateTimePicker.Type = enum_field(field_name='type')
  value_ms_epoch: Optional[str] = standard_field()
  timezone_offset_date: Optional[int] = standard_field()
  on_change_action: Optional[Action] = standard_field()
