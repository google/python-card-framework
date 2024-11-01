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
from typing import Any, Dict, List, Optional

import dataclasses_json
from card_framework import standard_field
from dataclasses_json import core

from .action import Action
from .open_link import OpenLink
from .overflow_menu import OverflowMenu


@dataclasses.dataclass
class OnClick(dataclasses_json.DataClassJsonMixin):
  """OnClick

  Renders an OnClick widget component.

  https://developers.google.com/chat/how-tos/cards-onclick
  """
  action: Action = standard_field()
  open_link: OpenLink = standard_field()

  overflow_menu: OverflowMenu = standard_field()

  open_dynamic_link_action: Action = standard_field()

  # Should be a `Card``, but it can't be done because of a circular
  # import
  card: Any = standard_field()

  def __setattr__(self, __name: str, __value: Any) -> None:
    """Sets attributes.

    This is overridden to ensure that one and only one of action and open_link
    can be set. If an attempt is made to set both, the already set one will be
    automatically cleared back to 'None'.

    If an attempt is being made to set a value to 'None', then no checks are
    performed, the value is just passed on.

    Args:
        __name (str): The name of the property to set.
        __value (Any): The value to set the property to.

    Returns:
        _type_: _description_
    """
    if __value:
      if __name == 'action':
        self.open_link = None
      elif __name == 'open_link':
        self.action = None

    super().__setattr__(__name, __value)

  def to_dict(self, encode_json=False) -> Dict[str, core.Json]:
    """Converts the dataclass to a dict.

    This is an override of the standard dataclass `to_dict` method to allow
    validation that `action` and `open_link` are mutually exclusive.

    Args:
        encode_json (bool, optional): encode the json strings. Defaults to False.

    Raises:
        ValueError: if both `action` and `open_link` are set.

    Returns:
        Dict[str, Json]: The header
    """
    if self.action and self.open_link:
      raise ValueError('Only one of action and open_link can be should be set.')

    return super().to_dict(encode_json)
