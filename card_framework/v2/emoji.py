# Copyright 2025 Google Inc. All Rights Reserved.
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
import dataclasses_json

from typing import Any, List, Dict
from card_framework import AutoNumber, enum_field, standard_field
from dataclasses_json import core


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class CustomEmojiPayload(object):
  file_content: str = standard_field()
  filename: str = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class CustomEmoji(object):
  name: str = standard_field()
  uid: str = standard_field()
  emoji_name: str = standard_field()
  temporary_image_uri: str = standard_field()
  payload: CustomEmojiPayload = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Emoji(object):
  unicode: str = standard_field()
  custom_emoji: CustomEmoji = standard_field()

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
      if __name == 'unicode':
        self.custom_emoji = None
      elif __name == 'custom_emoji':
        self.unicode = None

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
    if all([self.unicode, self.custom_emoji]):
      raise ValueError('Only one of [unicode, custom_emoji] can be set.')
    elif not (any([self.unicode, self.custom_emoji])):
      raise ValueError('One of [unicode, custom_emoji] must be set.')

    return super().to_dict(encode_json)


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EmojiReactionSummary(object):
  # class UserType(AutoNumber):
  #   TYPE_UNSPECIFIED = ()
  #   HUMAN = ()
  #   BOT = ()

  emoji: Emoji = standard_field()
  reaction_count: int = standard_field()
