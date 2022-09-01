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
from typing import Any, Dict, Mapping

import dataclasses_json
from card_framework import enum_field, standard_field
from dataclasses_json.core import Json

from .enums import Source


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclasses.dataclass
class Attachment(object):
  name: str = standard_field()
  content_name: str = standard_field()
  content_type: str = standard_field()
  thumbnail_uri: str = standard_field()
  download_uri: str = standard_field()
  source: Source = enum_field()

  attachment_data_ref: AttachmentDataRef = standard_field()
  drive_data_ref: DriveDataRef = standard_field()

  def __setattr__(self, __name: str, __value: Any) -> None:
    """Sets attributes.

    This is overridden to ensure that one and only one of action and open_link
    can be set. If an attempt is made to set both, the already set one will be
    automatically cleared back to 'None'.

    If an attempt is being made to set a value to 'None', then no checks are
    performed, the value is just passed on.

    Args:
        __name (str): The name of the property to set.
        __value (Any): The value to set the property to.

    Returns:
        _type_: _description_
    """
    if __value:
      if __name == 'drive_data_ref':
        self.attachment_data_ref = None
        self.type = Source.DRIVE_FILE
      elif __name == 'attachment_data_ref':
        self.drive_data_ref = None
        self.type = Source.UPLOADED_CONTENT

    super().__setattr__(__name, __value)

  def to_dict(self, encode_json=False) -> Dict[str, Json]:
    """Converts the dataclass to a dict.

    This is an override of the standard dataclass `to_dict` method to allow
    validation that `action` and `open_link` are mutually exclusive.

    Args:
        encode_json (bool, optional): encode the json strings. Defaults to False.

    Raises:
        ValueError: if both `known_icon` and `icon_url` are set.

    Returns:
        Dict[str, Json]: The header
    """
    if all([self.attachment_data_ref, self.drive_data_ref]):
      raise ValueError(
          'Only one of [attachmentDataRef, driveDataRef] can be set.')
    elif not(any([self.attachment_data_ref, self.drive_data_ref])):
      raise ValueError(f'One of [attachmentDataRef, driveDataRef] must be set.')

    return super().to_dict(encode_json)

  def render(self) -> Mapping[str, Any]:
    """Renders the response to json.

    Returns:
        Mapping[str, Any]: _description_
    """
    return {'attachment': self.to_dict(), }


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclasses.dataclass
class AttachmentDataRef(object):
  resource_name: str = standard_field()


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclasses.dataclass
class DriveDataRef(object):
  drive_file_id: str = standard_field()
