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

from dataclasses import dataclass, field
from typing import Any, List, Mapping

from card_framework import enum_field, list_field, standard_field, AutoNumber
from dataclasses_json import LetterCase, config, dataclass_json

from ..enums import HorizontalAlignment
from ..widget import Widget
from .color import Color
from .on_click import OnClick


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Grid(Widget):
  title: str = standard_field()
  items: List[GridItem] = list_field()
  border_style: BorderStyle = standard_field()
  column_count: int = standard_field()
  on_click: OnClick = standard_field()

  @property
  def _widget_tag(self) -> str:
    """The widget tag name.

    Returns:
        str: The key by which the widget will be rendered in the Section.
    """
    return 'grid'

  def render(self) -> Mapping[str, Any]:
    """Renders the response to json.

    Returns:
        Mapping[str, Any]: _description_
    """
    return {self._widget_tag: self.to_dict(), }


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GridItem(object):
  class GridItemLayout(AutoNumber):
    GRID_ITEM_LAYOUT_UNSPECIFIED = 'GRID_ITEM_LAYOUT_UNSPECIFIED'
    TEXT_BELOW = 'TEXT_BELOW'
    TEXT_ABOVE = 'TEXT_ABOVE'

  id: str = standard_field()
  image: ImageComponent = standard_field()
  title: str = standard_field()
  subtitle: str = standard_field()
  text_alignment: HorizontalAlignment = enum_field()
  layout: GridItemLayout = enum_field()


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ImageComponent(object):
  image_uri: str = standard_field()
  alt_text: str = standard_field()
  crop_style: ImageCropStyle = standard_field()
  border_style: BorderStyle = standard_field()


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ImageCropStyle(object):
  class ImageCropType(AutoNumber):
    IMAGE_CROP_TYPE_UNSPECIFIED = 'IMAGE_CROP_TYPE_UNSPECIFIED'
    SQUARE = 'SQUARE'
    CIRCLE = 'CIRCLE'
    RECTANGLE_CUSTOM = 'RECTANGLE_CUSTOM'
    RECTANGLE_4_3 = 'RECTANGLE_4_3'

  type: ImageCropType = enum_field()
  aspect_ratio: float = standard_field()


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BorderStyle(object):
  class BorderType(AutoNumber):
    BORDER_TYPE_UNSPECIFIED = 'BORDER_TYPE_UNSPECIFIED'
    NO_BORDER = 'NO_BORDER'
    STROKE = 'STROKE'

  type: BorderType = enum_field()
  stroke_color: Color = standard_field()
  corner_radius: int = standard_field()
