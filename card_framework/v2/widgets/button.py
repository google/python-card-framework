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
from dataclasses import dataclass
from typing import Any, Dict, Optional

from dataclasses_json import LetterCase, dataclass_json

from card_framework import standard_field

from ..widget import Widget
from .color import Color
from .icon import Icon
from .on_click import OnClick


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Button(object):
  """Button

  Renders a Button.

  https://developers.google.com/chat/api/guides/message-formats/cards#buttons
  """
  text: str = standard_field()
  icon: Icon = standard_field()
  color: Optional[Color] = standard_field()
  on_click: OnClick = standard_field()
  disabled: bool = standard_field()
  alt_text: str = standard_field()
