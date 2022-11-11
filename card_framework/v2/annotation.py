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
from typing import Any, Dict, Mapping

import card_framework
import dataclasses_json
from dataclasses_json.core import Json

from .user import User


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Annotation(card_framework.Renderable):
  class AnnotationType(card_framework.AutoNumber):
    ANNOTATION_TYPE_UNSPECIFIED = ()
    USER_MENTION = ()
    SLASH_COMMAND = ()

  type: AnnotationType = card_framework.enum_field()
  startIndex: int = card_framework.standard_field()
  length: int = card_framework.standard_field()
  user_mention: UserMentionMetadata = card_framework.standard_field()
  slash_command: SlashCommandMetadata = card_framework.standard_field()

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
      if __name == ():
        self.slash_command = None
      elif __name == ():
        self.user_mention = None

    super().__setattr__(__name, __value)

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
    if all([self.slash_command, self.user_mention]):
      raise ValueError('Only one of [slash_command, user_mention] can be set.')
    elif not (any([self.slash_command, self.user_mention])):
      raise ValueError(f'One of [slash_command, user_mention] must be set.')

    return super().to_dict(encode_json)


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclasses.dataclass
class UserMentionMetadata(object):
  class UserMentionMetadataType(card_framework.AutoNumber):
    TYPE_UNSPECIFIED = ()
    ADD = ()
    MENTION = ()

  user: User = card_framework.standard_field()
  type: UserMentionMetadataType = card_framework.enum_field()


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclasses.dataclass
class SlashCommandMetadata(object):
  class SlashCommandMetadataType(card_framework.AutoNumber):
    TYPE_UNSPECIFIED = ()
    ADD = ()
    INVOKE = ()

  bot: User = card_framework.standard_field()
  type: SlashCommandMetadataType = card_framework.enum_field()
  command_name: str = card_framework.standard_field()
  command_id: str = card_framework.standard_field()
  triggers_dialog: bool = card_framework.standard_field()
