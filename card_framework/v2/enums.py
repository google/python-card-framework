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
import enum

# Definite v2


class AutoNumber(enum.Enum):
  def __repr__(self):
    return '<%s.%s>' % (self.__class__.__name__, self.name)

  def __new__(cls, *args, **kwargs):
    value = len(cls.__members__) + 1
    obj = object.__new__(cls)
    obj._value_ = value
    return obj


class LoadIndicator(AutoNumber):
  """LoadIndicator
  """
  SPINNER = 'SPINNER'
  NONE = 'NONE'


class DisplayStyle(AutoNumber):
  DISPLAY_STYLE_UNSPECIFIED = 'DISPLAY_STYLE_UNSPECIFIED'
  PEEK = 'PEEK'
  REPLACE = 'REPLACE'


class ControlType(AutoNumber):
  SWITCH = 'SWITCH'
  CHECK_BOX = 'CHECK_BOX'

  @classmethod
  def _missing_(cls, value) -> ControlType:
    """Backward compatilbility for old enums.

    If the old product names are still in use, replace them with
    the new values seamlessly.

    Args:
        value (str): enum string value requested

    Returns:
        ControlType: the corrected type

    Raises:
        ValueError if it was simply an incorrect enum rather an old value
    """
    if value == 'CHECKBOX':
      # Deprecated in favor of CHECK_BOX.
      return cls.CHECK_BOX


class ImageType(AutoNumber):
  """ImageType

  The possible image styles of a Header image.
  """
  SQUARE = 'SQUARE'
  CIRCLE = 'CIRCLE'


class SelectionInputType(AutoNumber):
  """SelectionInputType
  """
  SWITCH = 'SWITCH'
  CHECK_BOX = 'CHECK_BOX'
  RADIO_BUTTON = 'RADIO_BUTTON'
  DROPDOWN = 'DROPDOWN'

# Unknown


class ImageStyle(AutoNumber):
  """ImageStyle

  The possible image styles of a Header image.
  """
  AVATAR = 'AVATAR'
  IMAGE = 'IMAGE'


class Icon(AutoNumber):
  """Icon

  The allowed built in icon values.

  https://developers.google.com/chat/api/guides/message-formats/cards#builtinicons
  """
  AIRPLANE = 'AIRPLANE'
  BOOKMARK = 'BOOKMARK'
  BUS = 'BUS'
  CAR = 'CAR'
  CLOCK = 'CLOCK'
  CONFIRMATION_NUMBER_ICON = 'CONFIRMATION_NUMBER_ICON'
  DESCRIPTION = 'DESCRIPTION'
  DOLLAR = 'DOLLAR'
  EMAIL = 'EMAIL'
  EVENT_SEAT = 'EVENT_SEAT'
  FLIGHT_ARRIVAL = 'FLIGHT_ARRIVAL'
  FLIGHT_DEPARTURE = 'FLIGHT_DEPARTURE'
  HOTEL = 'HOTEL'
  HOTEL_ROOM_TYPE = 'HOTEL_ROOM_TYPE'
  INVITE = 'INVITE'
  MAP_PIN = 'MAP_PIN'
  MEMBERSHIP = 'MEMBERSHIP'
  MULTIPLE_PEOPLE = 'MULTIPLE_PEOPLE'
  PERSON = 'PERSON'
  PHONE = 'PHONE'
  RESTAURANT_ICON = 'RESTAURANT_ICON'
  SHOPPING_CART = 'SHOPPING_CART'
  STAR = 'STAR'
  STORE = 'STORE'
  TICKET = 'TICKET'
  TRAIN = 'TRAIN'
  VIDEO_CAMERA = 'VIDEO_CAMERA'
  VIDEO_PLAY = 'VIDEO_PLAY'


class HorizontalAlignment(AutoNumber):
  """HorizontalAlignment
  """
  START = 'START'
  CENTER = 'CENTER'
  END = 'END'

  def __str__(self) -> str:
    return self.name

  def __repr__(self) -> str:
    return str(self.name)


class TextInputType(AutoNumber):
  """TextInputType
  """
  SINGLE_LINE = 'SINGLE_LINE'
  MULTIPLE_LINE = 'MULTIPLE_LINE'


class OnClose(AutoNumber):
  """OnClose
  """
  NOTHING = 'NOTHING'
  RELOAD = 'RELOAD'


class OpenAs(AutoNumber):
  """OpenAs
  """
  FULL_SIZE = 'FULL_SIZE'
  OVERLAY = 'OVERLAY'


class Code(AutoNumber):
  OK = 'OK'
  CANCELLED = 'CANCELLED'
  UNKNOWN = 'UNKNOWN'
  INVALID_ARGUMENT = 'INVALID_ARGUMENT'
  DEADLINE_EXCEEDED = 'DEADLINE_EXCEEDED'
  NOT_FOUND = 'NOT_FOUND'
  ALREADY_EXISTS = 'ALREADY_EXISTS'
  PERMISSION_DENIED = 'PERMISSION_DENIED'
  UNAUTHENTICATED = 'UNAUTHENTICATED'
  RESOURCE_EXHAUSTED = 'RESOURCE_EXHAUSTED'
  FAILED_PRECONDITION = 'FAILED_PRECONDITION'
  ABORTED = 'ABORTED'
  OUT_OF_RANGE = 'OUT_OF_RANGE'
  UNIMPLEMENTED = 'UNIMPLEMENTED'
  INTERNAL = 'INTERNAL'
  UNAVAILABLE = 'UNAVAILABLE'
  DATA_LOSS = 'DATA_LOSS'


class ResponseType(AutoNumber):
  TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'
  NEW_MESSAGE = 'NEW_MESSAGE'
  UPDATE_MESSAGE = 'UPDATE_MESSAGE'
  UPDATE_USER_MESSAGE_CARDS = 'UPDATE_USER_MESSAGE_CARDS'
  REQUEST_CONFIG = 'REQUEST_CONFIG'
  DIALOG = 'DIALOG'


class UserType(AutoNumber):
  TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'
  HUMAN = 'HUMAN'
  BOT = 'BOT'


class AnnotationType(AutoNumber):
  ANNOTATION_TYPE_UNSPECIFIED = 'ANNOTATION_TYPE_UNSPECIFIED'
  USER_MENTION = 'USER_MENTION'
  SLASH_COMMAND = 'SLASH_COMMAND'


class SpaceType(AutoNumber):
  SPACE_TYPE_UNSPECIFIED = 'SPACE_TYPE_UNSPECIFIED'
  SPACE = 'SPACE'
  GROUP_CHAT = 'GROUP_CHAT'
  DIRECT_MESSAGE = 'DIRECT_MESSAGE'


class Source(AutoNumber):
  SOURCE_UNSPECIFIED = 'SOURCE_UNSPECIFIED'
  DRIVE_FILE = 'DRIVE_FILE'
  UPLOADED_CONTENT = 'UPLOADED_CONTENT'
