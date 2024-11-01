# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations

from card_framework import AutoNumber, string_enum
from enum import auto

# enums.py
#
# Generic enums, reused in multiple classes. Most enums are widget specific,
# so are defined in that widget.


class ImageType(AutoNumber):
  """ImageType

  The possible image styles of a Header image.
  """
  SQUARE = auto()
  CIRCLE = auto()


class HorizontalAlignment(AutoNumber):
  """HorizontalAlignment
  """
  HORIZONTAL_ALIGNMENT_UNSPECIFIED = ()
  START = ()
  CENTER = ()
  END = ()
