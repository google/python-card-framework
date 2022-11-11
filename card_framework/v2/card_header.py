# Copyright 2022 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import dataclasses
from typing import Dict, Optional

import dataclasses_json
from card_framework import enum_field, standard_field
from dataclasses_json import core

from .enums import ImageType


@dataclasses.dataclass
class CardHeader(dataclasses_json.DataClassJsonMixin):
  """CardHeader

  Describes a Google Chat App response header.

  https://developers.google.com/chat/api/reference/rest/v1/cards#cardheader
  """
  title: Optional[str] = standard_field()
  subtitle: Optional[str] = standard_field()
  image_url: Optional[str] = standard_field()
  image_type: Optional[ImageType] = enum_field()
  image_alt_text: Optional[str] = standard_field()

  def to_dict(self, encode_json=False) -> Dict[str, core.Json]:
    """Converts the dataclass to a dict.

    This is an override of the standard dataclass `to_dict` method to allow
    validation that `image_style` is set if `image_url` is provided.

    Args:
        encode_json (bool, optional): encode the json strings. Defaults to False.

    Raises:
        ValueError: if the `image_style` is not set with the `image_url`

    Returns:
        Dict[str, Json]: The header
    """
    if self.image_url and not self.image_type:
      raise ValueError('If image_url is used, image_style must be set.')

    return super().to_dict(encode_json)
