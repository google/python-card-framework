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

import inspect
from dataclasses import dataclass, field
from typing import Any, Mapping, Optional

import dataclasses_json
import stringcase
from card_framework import standard_field
from dataclasses_json.core import Json

from .enums import HorizontalAlignment


@dataclass
class Widget(dataclasses_json.DataClassJsonMixin):
  """Widget

  Parent class to all widgets. Each child Widget must implement the
  `_widget_tag` property which is the key the Section.widgets list will name
  the rendered widget map.
  """
  _horizontal_alignment: HorizontalAlignment = \
      standard_field(exclude=lambda x: True)
  # field(
  #     default=None, metadata=dataclasses_json.config(
  #         exclude=lambda x: not False))

  @property
  def horizontal_alignment(self) -> str:
    return \
        self._horizontal_alignment.name if self._horizontal_alignment else None

  @horizontal_alignment.setter
  def horizontal_alignment(self, a: HorizontalAlignment = None) -> None:
    self._horizontal_alignment = a

  @property
  def _widget_tag(self) -> str:
    """The widget tag name.

    Raises:
        NotImplementedError: If not implemented.

    Returns:
        str: The key by which the widget will be rendered in the Section.
    """
    raise NotImplementedError('All widgets must provide their tag name.')

  def render(self) -> Mapping[str, Any]:
    """Renders the widget in a usable form.

    Returns:
        Mapping[str, Any]: the json representation of the widget
    """
    render = {}
    properties = inspect.getmembers(self.__class__,
                                    lambda v: isinstance(v, property))
    for (name, value) in properties:
      if name == '_widget_tag':
        render[self._widget_tag] = self.to_dict()
      else:
        if widget_value := value.fget(self):
          render[stringcase.camelcase(name)] = widget_value

    return render
