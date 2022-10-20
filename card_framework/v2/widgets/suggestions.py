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
from typing import Any, Dict, List, Optional

from card_framework import standard_field

from ..enums import Icon, TextInputType
from dataclasses_json import DataClassJsonMixin, LetterCase, config, dataclass_json
from dataclasses_json.core import Json

from .action import Action
from .on_click import OnClick
from ..widget import Widget

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuggestionItem(object):
  text: str = standard_field()

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Suggestions(object):
  items: List[SuggestionItem] = standard_field()
