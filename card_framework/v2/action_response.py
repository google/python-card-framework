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
from card_framework import AutoNumber, Renderable, enum_field, standard_field

from .dialog_action import DialogAction


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ActionResponse(Renderable):
  class ResponseType(AutoNumber):
    TYPE_UNSPECIFIED = ()
    NEW_MESSAGE = ()
    UPDATE_MESSAGE = ()
    UPDATE_USER_MESSAGE_CARDS = ()
    REQUEST_CONFIG = ()
    DIALOG = ()

  type: ResponseType = enum_field()
  url: str = standard_field()
  dialog_action: DialogAction = standard_field()
