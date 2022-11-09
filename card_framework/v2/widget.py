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
from card_framework import Renderable, enum_field

from .enums import HorizontalAlignment


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Widget(Renderable):
  """Widget
  """
  __horizontal_alignment: HorizontalAlignment = enum_field(
    exclude=lambda x: True)

  @property
  def horizontal_alignment(self) -> str:
    return \
        self.__horizontal_alignment.name if self.__horizontal_alignment else None

  @horizontal_alignment.setter
  def horizontal_alignment(self, a: HorizontalAlignment = None) -> None:
    self.__horizontal_alignment = a
