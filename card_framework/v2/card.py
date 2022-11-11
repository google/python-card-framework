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
import uuid
from typing import List, Optional

import dataclasses_json
from card_framework import AutoNumber, Renderable, list_field, standard_field

from .card_action import CardAction
from .card_fixed_footer import CardFixedFooter
from .card_header import CardHeader
from .section import Section


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class RenderableCard(Renderable):
  __card_id = None

  @property
  def card_id(self) -> str:
    return self.__card_id if self.__card_id else str(uuid.uuid4())

  @card_id.setter
  def card_id(self, value: str) -> None:
    self.__card_id = value

  card: Card = standard_field(exclude=lambda x: True)


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Card(RenderableCard):
  """Response

  A response object that can be `render`ed to produce a valid Google Chat App
  json response.

  See https://developers.google.com/chat/api/guides/message-formats/cards for
  full details on what this should look like.
  """
  class DisplayStyle(AutoNumber):
    DISPLAY_STYLE_UNSPECIFIED = ()
    PEEK = ()
    REPLACE = ()

  header: Optional[CardHeader] = standard_field()
  name: Optional[str] = standard_field()
  sections: Optional[List[Section]] = list_field(default_factory=list)
  card_actions: Optional[List[CardAction]] = standard_field()
  fixed_footer: Optional[CardFixedFooter] = standard_field()
  display_style: Optional[DisplayStyle] = standard_field()
  peek_card_header: Optional[CardHeader] = standard_field()

  def add_section(self, section: Section) -> None:
    """Adds a section to the report.

    Args:
        section (Section): The section to add.
    """
    self.sections.append(section)
