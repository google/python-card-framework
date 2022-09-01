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
from dataclasses import dataclass, field
from typing import Any, Dict, List, Mapping, Optional

from dataclasses_json import DataClassJsonMixin, config
from dataclasses_json.core import Json

from card_framework import list_field, standard_field

from .widget import Widget


@dataclass
class Section(DataClassJsonMixin):
  """Section

  Describes a Google Chat App response Section.

  https://developers.google.com/chat/api/guides/message-formats/cards#sections_and_widgets
  """

  # def render_widgets(self, x) -> Dict[str, Json]:
  #   return [widget.render() for widget in x]

  header: Optional[str] = standard_field()
  widgets: Optional[List[Widget]] = list_field(default_factory=list)
  collapsible: bool = standard_field()
  uncollapsible_widgets_count: int = standard_field()

  def add_widget(self, widget: Widget) -> None:
    """Adds a widget to the section.

    Widgets need to be added in a specific way, including the tag. Simply adding
    a widget object to the `List` of widgets is not sufficient. As a result this
    helper method should be used for safety. This uses the built in widget's
    attribute `_widget_tag` which will ensure the widget is rendered correctly
    when necessary.

    Args:
        widget (Widget): The widget to be added to the section.
    """
    self.widgets.append(widget)

  def render(self) -> Mapping[str, Any]:
    """Renders the response to json.

    Returns:
        Mapping[str, Any]: _description_
    """
    return self.to_dict()
