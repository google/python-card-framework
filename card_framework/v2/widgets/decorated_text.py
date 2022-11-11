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
from typing import Dict, Optional

import dataclasses_json
from card_framework import standard_field
from dataclasses_json.core import Json

from ..widget import Widget
from .button import Button
from .icon import Icon
from .on_click import OnClick
from .switch_control import SwitchControl


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class DecoratedText(Widget):
  """DecoratedText

  This will render a DecoratedText widget.

  https://developers.google.com/chat/api/guides/message-formats/cards#decoratedtext
  """
  icon: Optional[Icon] = standard_field()
  start_icon: Optional[Icon] = standard_field()
  top_label: str = standard_field()
  text: str = standard_field()
  wrap_text: bool = standard_field()
  bottom_label: str = standard_field()
  on_click: Optional[OnClick] = standard_field()
  button: Optional[Button] = standard_field()
  switch_control: Optional[SwitchControl] = standard_field()
  end_icon: Optional[Icon] = standard_field()

  def to_dict(self, encode_json=False) -> Dict[str, Json]:
    """Converts the dataclass to a dict.

    This is an override of the standard dataclass `to_dict` method to allow
    validation that `action` and `open_link` are mutually exclusive.

    Args:
        encode_json (bool, optional): encode the json strings. Defaults to False.

    Raises:
        ValueError: if both `known_icon` and `icon_url` are set.

    Returns:
        Dict[str, Json]: The header
    """
    if sum(i is not None
           for i in [self.button, self.switch_control, self.end_icon]) > 1:
      raise ValueError(
          'Only one of [button, switch_control, end_icon] can be set.')

    return super().to_dict(encode_json)
