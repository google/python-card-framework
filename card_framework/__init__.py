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
from typing import Any, Mapping, TypeVar, Type

import dataclasses_json
import stringcase
from marshmallow import fields


def __field(default: Any = None, default_factory: Any = None,
            **metadata) -> dataclasses.Field:
  return (
      dataclasses.field(
          default_factory=default_factory,
          metadata=dataclasses_json.config(**metadata)
      ) if default_factory
      else dataclasses.field(default=default,
                             metadata=dataclasses_json.config(**metadata))
  )


def merge_metadata(base: Mapping[str, Any], **custom) -> Mapping[str, Any]:
  """Merges metadata with supplied metadata keys.

  This is different from a plain dict.update() as it removes keys defined as
  `None` allowing any dataclass default behaviour to reassert itself.

  Args:
      base (Mapping[str, Any]): the base metadata
      **custom (Any): the list of named metadata parameters to add/edit/remove

  Returns:
      Mapping[str, Any]: the merged metadata
  """
  for key in custom:
    if not custom[key] and key in base:
      del base[key]

    elif custom[key]:
      base |= {key: custom[key]}

  return base


def standard_field(default: Any = None, default_factory: Any = None,
                   **kwargs) -> dataclasses.Field:
  base = merge_metadata({
      'letter_case': dataclasses_json.LetterCase.CAMEL,
      'exclude': lambda x: not x
  }, **kwargs)

  return __field(default=default, default_factory=default_factory, **base)


def enum_field(default: Any = None, **kwargs) -> dataclasses.Field:
  base = {
      'encoder': lambda x: x.name if x else None,
      **kwargs
  }

  return standard_field(default=default, **base)


def list_field(default_factory: Any = list,
               **kwargs) -> dataclasses.Field:
  def __value(f: Any) -> Any:
    for a in ['render', 'to_dict']:
      if (m := getattr(f, a, None)) and callable(m):
        return m()

  base = {'encoder': lambda x: [__value(f) or f for f in x], **kwargs}

  return standard_field(default_factory=default_factory, **base)


E = TypeVar('E', bound=enum.Enum)
def string_enum(cls: Type[E]) -> Type[E]:
  class EnumField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
      return value.name

    def _deserialize(self, value, attr, data, **kwargs):
      return cls[value]

  if (not hasattr(cls, '__metadata__')):
    setattr(cls, '__metadata__', dict())

  metadata = {
      "dataclasses_json": {
          "encoder": lambda v: v.name if v else None,
          "decoder": lambda name: cls[name],
          "mm_field": EnumField(),
      }
  }

  cls.__metadata__.update(metadata)
  return cls

@string_enum
class AutoNumber(enum.Enum):
  def __repr__(self):
    return f'{self.name}'

  def __new__(cls, *args, **kwargs):
    value = len(cls.__members__) + 1
    obj = object.__new__(cls)
    obj._value_ = value
    return obj

  @classmethod
  def _missing_(cls, value):
    return cls[value]


class Renderable(object):
  """Renderable adds a 'render' method to subclasses objects.

  Subclasses can also define the following special values, which can be set
  at runtime by the user as well if need be (although I can't think why):
  __SUPPRESS_TAG__ (bool)
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
    __SUPPRESS_TAG__ = True
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
    if getattr(self, '__SUPPRESS_TAG__', False):
      return self.to_dict()

    render = {
        (getattr(self, '__OVERRIDE_TAG__', False) or
         stringcase.camelcase(self.__class__.__name__)): self.to_dict()}
    properties = inspect.getmembers(self.__class__,
                                    lambda v: isinstance(v, property))
    for (name, value) in properties:
      if widget_value := value.fget(self):
        render[stringcase.camelcase(name)] = widget_value

    return render
