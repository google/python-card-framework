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
from typing import Optional

from dataclasses_json import LetterCase, dataclass_json

from card_framework import standard_field

from .on_click import OnClick
from ..widget import Widget


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Image(Widget):
  """Image widget.

  Renders an Image widget

  https://developers.google.com/chat/api/reference/rest/v1/cards#image
  """
  image_url: str = standard_field()
  on_click: Optional[OnClick] = standard_field()
  alt_text: str = standard_field()

  @property
  def _widget_tag(self) -> str:
    """The widget tag name.

    Returns:
        str: The key by which the widget will be rendered in the Section.
    """
    return 'image'
