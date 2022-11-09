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
from typing import List, Optional

from card_framework import Renderable, list_field, standard_field
from dataclasses_json import dataclass_json

from .widget import Widget


@dataclass_json
@dataclass
class Section(Renderable):
  """Section

  Describes a Google Chat App response Section.

  https://developers.google.com/chat/api/guides/message-formats/cards#sections_and_widgets
  """
  __no_root_level__ = True

  header: Optional[str] = standard_field()
  widgets: Optional[List[Widget]] = list_field(default_factory=list)
  collapsible: bool = standard_field()
  uncollapsible_widgets_count: int = standard_field()

  def add_widget(self, widget: Widget) -> None:
    """Adds a widget to the section.

    A helper to replicate section.widgets.append(<widget>) as this can be
    more readable and apparent to an end user.

    Args:
        widget (Widget): The widget to be added to the section.
    """
    self.widgets.append(widget)
