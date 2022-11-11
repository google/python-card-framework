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

import dataclasses_json
from card_framework import AutoNumber, enum_field, standard_field

from ..widget import Widget
from .action import Action


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class SwitchControl(Widget):
  """SwitchControl
  """
  class ControlType(AutoNumber):
    """ControlType _summary_
_
    """
    SWITCH = ()
    CHECK_BOX = ()

    @classmethod
    def _missing_(cls, value) -> SwitchControl.ControlType:
      """Backward compatilbility for old enums.

      If the old product names are still in use, replace them with
      the new values seamlessly.

      Args:
          value (str): enum string value requested

      Returns:
          ControlType: the corrected type

      Raises:
          ValueError if it was simply an incorrect enum rather an old value
      """
      if value == 'CHECKBOX':
        # Deprecated in favor of CHECK_BOX.
        return cls.CHECK_BOX

  name: str = standard_field(default='')
  value: str = standard_field(default='')
  selected: bool = standard_field(default=None)
  onChangeAction: Action = standard_field(default=None)
  controlType: ControlType = enum_field()
