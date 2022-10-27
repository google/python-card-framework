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
from typing import Any, Mapping

import dataclasses_json
from card_framework import AutoNumber, enum_field, standard_field

from .dialog_action import DialogAction


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclasses.dataclass
class ActionResponse(object):
  class ResponseType(AutoNumber):
    TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'
    NEW_MESSAGE = 'NEW_MESSAGE'
    UPDATE_MESSAGE = 'UPDATE_MESSAGE'
    UPDATE_USER_MESSAGE_CARDS = 'UPDATE_USER_MESSAGE_CARDS'
    REQUEST_CONFIG = 'REQUEST_CONFIG'
    DIALOG = 'DIALOG'

  _tag = 'actionResponse'

  @property
  def tag(self) -> str:
    return self._tag

  @tag.setter
  def tag(self, value: str) -> None:
    self._tag = value

  type: ResponseType = enum_field()
  url: str = standard_field()
  dialog_action: DialogAction = standard_field()

  def render(self) -> Mapping[str, Any]:
    """Renders the response to json.

    Returns:
        Mapping[str, Any]: _description_
    """

    return {self.tag: self.to_dict()}
