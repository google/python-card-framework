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
from typing import List

import dataclasses_json
from card_framework import AutoNumber, enum_field, list_field, standard_field

from ..enums import HorizontalAlignment
from ..widget import Widget
from .color import Color
from .on_click import OnClick


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Grid(Widget):
  title: str = standard_field()
  items: List[GridItem] = list_field()
  border_style: BorderStyle = standard_field()
  column_count: int = standard_field()
  on_click: OnClick = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class GridItem(object):
  class GridItemLayout(AutoNumber):
    GRID_ITEM_LAYOUT_UNSPECIFIED = ()
    TEXT_BELOW = ()
    TEXT_ABOVE = ()

  id: str = standard_field()
  image: ImageComponent = standard_field()
  title: str = standard_field()
  subtitle: str = standard_field()
  text_alignment: HorizontalAlignment = enum_field()
  layout: GridItemLayout = enum_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ImageComponent(object):
  image_uri: str = standard_field()
  alt_text: str = standard_field()
  crop_style: ImageCropStyle = standard_field()
  border_style: BorderStyle = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ImageCropStyle(object):
  class ImageCropType(AutoNumber):
    IMAGE_CROP_TYPE_UNSPECIFIED = ()
    SQUARE = ()
    CIRCLE = ()
    RECTANGLE_CUSTOM = ()
    RECTANGLE_4_3 = ()

  type: ImageCropType = enum_field()
  aspect_ratio: float = standard_field()


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class BorderStyle(object):
  class BorderType(AutoNumber):
    BORDER_TYPE_UNSPECIFIED = ()
    NO_BORDER = ()
    STROKE = ()

  type: BorderType = enum_field()
  stroke_color: Color = standard_field()
  corner_radius: int = standard_field()
