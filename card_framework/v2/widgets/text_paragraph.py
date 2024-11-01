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
import dataclasses

import dataclasses_json
from card_framework import standard_field

from ..widget import Widget


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class TextParagraph(Widget):
  """TextParagraph

  This will render a TextParagraph widget.

  https://developers.google.com/chat/api/guides/message-formats/cards#textparagraph
  """
  text: str = standard_field()
  max_lines: int = standard_field()
