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
from typing import Any, Dict, Iterable, Mapping

from  card_framework import enum_field, standard_field
import dataclasses_json
from dataclasses_json.core import Json

from .enums import SpaceType


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclasses.dataclass
class Space(object):
  name: str = standard_field()
  type: str = standard_field() # deprecated
  spaceType: SpaceType = enum_field()
  singleUserBotDm: bool = standard_field()
  threaded: bool = standard_field()
  displayName: str = standard_field()
  spaceDetails: SpaceDetail = standard_field()


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclasses.dataclass
class SpaceDetail(object):
  description: str = standard_field()
  guidelines: str = standard_field()
