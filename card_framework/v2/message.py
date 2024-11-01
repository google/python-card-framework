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
from typing import Any, List, Mapping, Optional

import dataclasses_json
from card_framework import Renderable, list_field, standard_field

from .action_response import ActionResponse
from .annotation import Annotation
from .attachment import Attachment
from .card import Card
from .space import Space
from .user import User


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Message(Renderable):
  __SUPPRESS_TAG__ = True

  name: str = standard_field()
  sender: User = standard_field()
  create_time: str = standard_field()
  last_update_time: str = standard_field()
  text: str = standard_field()
  cards: List[Card] = list_field(field_name='cardsV2')
  annotations: List[Annotation] = list_field()
  thread: Thread = standard_field()
  space: Space = standard_field()
  fallback_text: str = standard_field()
  action_response: ActionResponse = standard_field()
  argument_text: str = standard_field()
  slashCommand: SlashCommand = standard_field()
  attachment: List[Attachment] = list_field()
  matchedUrl: MatchedUrl = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Thread(object):
  name: str = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class SlashCommand(object):
  commandId: str = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class MatchedUrl(object):
  url: str = standard_field()
