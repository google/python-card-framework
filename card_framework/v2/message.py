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
from .emoji import EmojiReactionSummary
from .user import User
from .space import Space
from .card import Card, CardWithId
from .attachment import Attachment
from .annotation import Annotation
from .action_response import ActionResponse
from .widgets.button_list import ButtonList

import dataclasses
from typing import Any, List, Mapping, Optional

import dataclasses_json
from card_framework import AutoNumber, Renderable, list_field
from card_framework import standard_field, enum_field


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Message(Renderable):
  __SUPPRESS_TAG__ = True

  name: str = standard_field()
  sender: User = standard_field()
  create_time: str = standard_field()
  last_update_time: str = standard_field()
  delete_time: str = standard_field()
  text: str = standard_field()
  cards: List[Card] = list_field()
  cards_v2: List[CardWithId] = list_field(
      letter_case=dataclasses_json.LetterCase.SNAKE)
  annotations: List[Annotation] = list_field()
  thread: Thread = standard_field()
  space: Space = standard_field()
  fallback_text: str = standard_field()
  action_response: ActionResponse = standard_field()
  argument_text: str = standard_field()
  slash_command: SlashCommand = standard_field()
  attachment: List[Attachment] = list_field()
  matched_url: MatchedUrl = standard_field()
  thread_reply: bool = standard_field()
  client_assigned_message_id: str = standard_field()
  emoji_reaction_summaries: List[EmojiReactionSummary] = list_field()
  private_message_viewer: User = standard_field()
  deletion_metadata: DeletionMetaData = standard_field()
  quoted_message_metadata: QuotedMessageMetadata = standard_field()
  attached_gifs: List[AttachedGif] = list_field()
  accessory_widgets: List[AccessoryWidget] = list_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Thread(object):
  name: str = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class SlashCommand(object):
  command_id: str = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class MatchedUrl(object):
  url: str = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class DeletionMetadata(object):
  class DeletionType(AutoNumber):
    DELETION_TYPE_UNSPECIFIED = ()
    CREATOR = ()
    SPACE_OWNER = ()
    ADMIN = ()
    APP_MESSAGE_EXPIRY = ()
    CREATOR_VIA_APP = ()
    SPACE_OWNER_VIA_APP = ()

  deletion_type: DeletionType = enum_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class QuotedMessageMetadata(object):
  name: str = standard_field()
  last_update_time: str = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class AttachedGif(object):
  uri: str = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class AccessoryWidget(object):
  button_list: ButtonList = standard_field()
