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
from typing import Any, Dict, Optional

import dataclasses_json
from card_framework import AutoNumber, enum_field, standard_field
from dataclasses_json import core

from ..enums import ImageType


@dataclasses.dataclass
class Icon(dataclasses_json.DataClassJsonMixin):
  class KnownIcon(AutoNumber):
    """Icon

    The allowed built in icon values.

    https://developers.google.com/chat/api/guides/message-formats/cards#builtinicons
    """
    AIRPLANE = ()
    BOOKMARK = ()
    BUS = ()
    CAR = ()
    CLOCK = ()
    CONFIRMATION_NUMBER_ICON = ()
    DESCRIPTION = ()
    DOLLAR = ()
    EMAIL = ()
    EVENT_SEAT = ()
    FLIGHT_ARRIVAL = ()
    FLIGHT_DEPARTURE = ()
    HOTEL = ()
    HOTEL_ROOM_TYPE = ()
    INVITE = ()
    MAP_PIN = ()
    MEMBERSHIP = ()
    MULTIPLE_PEOPLE = ()
    PERSON = ()
    PHONE = ()
    RESTAURANT_ICON = ()
    SHOPPING_CART = ()
    STAR = ()
    STORE = ()
    TICKET = ()
    TRAIN = ()
    VIDEO_CAMERA = ()
    VIDEO_PLAY = ()

  @dataclasses.dataclass
  class MaterialIcon(dataclasses_json.DataClassJsonMixin):
    """MaterialIcon
    """
    name: Optional[str] = standard_field()
    fill: Optional[bool] = standard_field()
    weight: Optional[int] = standard_field()
    grade: Optional[int] = standard_field()

  alt_text: Optional[str] = standard_field()
  image_type: Optional[ImageType] = enum_field()
  known_icon: Optional[KnownIcon] = enum_field()
  icon_url: Optional[str] = standard_field()
  material_icon: Optional[MaterialIcon] = standard_field()

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
      if __name == 'known_icon':
        self.icon_url = None
      elif __name == 'icon_url':
        self.known_icon = None

    super().__setattr__(__name, __value)

  def to_dict(self, encode_json=False) -> Dict[str, core.Json]:
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
    if all([self.known_icon, self.icon_url, self.material_icon]):
      raise ValueError('Only one of [known_icon, icon_url, '
                       'material_icon] can be set.')
    elif not (any([self.known_icon, self.icon_url, self.material_icon])):
      raise ValueError('One of [known_icon, icon_url, '
                       'material_icon] must be set.')

    return super().to_dict(encode_json)
