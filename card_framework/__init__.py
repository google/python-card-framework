# Copyright 2022 Google LLC
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

import dataclasses
import enum
import inspect
import stringcase
from typing import Any, Callable, List, Mapping

import dataclasses_json


def lazy_property(f: Callable):
  """Decorator that makes a property lazy-evaluated.

  Args:
    f: the function to convert to a lazy property.
  """
  attr_name = '_lazy_' + f.__name__

  @property
  def _lazy_property(self) -> Any:
    if not hasattr(self, attr_name):
      setattr(self, attr_name, f(self))
    return getattr(self, attr_name)
  return _lazy_property


def field(default: Any = None, default_factory: Any = None,
          **metadata) -> dataclasses.Field:
  return (
      dataclasses.field(
          default_factory=default_factory,
          metadata=dataclasses_json.config(**metadata)
      ) if default_factory
      else dataclasses.field(default=default,
                             metadata=dataclasses_json.config(**metadata))
  )


def metadata(base: Mapping[str, Any], **custom) -> Mapping[str, Any]:
  for key in custom:
    if not custom[key] and key in base:
      del base[key]

    elif custom[key]:
      base.update({key: custom[key]})

  return base


def standard_field(default: Any = None, default_factory: Any = None,
                   **kwargs) -> dataclasses.Field:
  base = metadata({
      'letter_case': dataclasses_json.LetterCase.CAMEL,
      'exclude': lambda x: not x
  }, **kwargs)

  return field(default=default, default_factory=default_factory, **base)


def enum_field(default: Any = None, **kwargs) -> dataclasses.Field:
  base = {'encoder': lambda x: x.name if x else None, **kwargs}

  return standard_field(default=default, **base)


def list_field(default_factory: Any = list,
               **kwargs) -> dataclasses.Field:
  def __value(f: Any) -> Any:
    for a in ['render', 'to_dict']:
      if (m := getattr(f, a, None)) and callable(m):
        return m()

  base = {'encoder': lambda x: [__value(f) or f for f in x], **kwargs}

  return standard_field(default_factory=default_factory, **base)


class AutoNumber(enum.Enum):
  def __repr__(self):
    return f'{self.__class__.__name__}, {self.name}'

  def __new__(cls, *args, **kwargs):
    value = len(cls.__members__) + 1
    obj = object.__new__(cls)
    obj._value_ = value
    return obj


class Renderable(object):
  """Renderable adds a 'render' method to subclasses objects.

  Subclasses can also define the following special values, which can be set
  at runtime by the user as well if need be (although I can't think why):
  __NO_TAG_NAME__ (bool)
    This causes the render method to behave like `to_dict`.

  __TAG_OVERRIDE__ (str)
    Renames the root tag from the camelCase class name to the specified string.

  Thus, given a fragment like this:
  ```
  class SampleWidget(Renderable):
    sample_tag: str = standard_field()

  s = Sample(sample_tag='Hello, my name is Inigo Montoya.')
  s.render()
  ```
  you would get
  `{'sampleWidget': {'sampleTag': 'Hello, my name is Inigo Montoya.'}}`

  However if `SampleWidget` were defined as:
  ```
  class SampleWidget(Renderable):
    __NO_TAG_NAME__ = True
    sample_tag: str = standard_field()
  ```
  you'd get
  `{'sampleTag': 'Hello, my name is Inigo Montoya.'}`

  If it had the override set, thus:
  ```
  class SampleWidget(Renderable):
    __TAG_OVERRIDE__ = 'aSampleWidgetClass'
    sample_tag: str = standard_field()
  ```
  the `render` command would produce
  `{'aSampleWidgetClass': {'sampleTag': 'Hello, my name is Inigo Montoya.'}}`

  NOTE: the __TAG_OVERRIDE is *NOT* camel-cased. What you enter is what you get.

  A subclass can implement their own `render` method, but it must return the
  valid Chat API JSON. An examnple of this is the `Card` class which has to add
  the `cardId` tag level with the `card` itself at the JSON top level.
  """

  def render(self) -> Mapping[str, Any]:
    """Renders the widget in a usable form.

    Returns:
        Mapping[str, Any]: the json representation of the widget
    """
    if getattr(self, '__NO_TAG_NAME__', False):
      return self.to_dict()

    render = {
        (getattr(self, '__TAG_OVERRIDE__', False) or
          stringcase.camelcase(self.__class__.__name__)): self.to_dict()}
    properties = inspect.getmembers(self.__class__,
                                    lambda v: isinstance(v, property))
    for (name, value) in properties:
      if widget_value := value.fget(self):
        render[stringcase.camelcase(name)] = widget_value

    return render
