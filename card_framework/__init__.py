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
import enum
import inspect
from typing import Any, Callable, Mapping

import dataclasses_json
import dataclasses


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
  return \
      dataclasses.field(default_factory=default_factory,
                        metadata=dataclasses_json.config(**metadata)) \
      if default_factory else \
      dataclasses.field(default=default,
                        metadata=dataclasses_json.config(**metadata))


def metadata(base: Mapping[str, Any], **custom) -> Mapping[str, Any]:
  for key in custom:
    if not custom[key] and key in base:
      del base[key]

    elif custom[key]:
      base.update({key: custom[key]})

  return base


def standard_field(default: Any = None, default_factory: Any = None,
                   **kwargs) -> dataclasses.Field:
  base = {
      'letter_case': dataclasses_json.LetterCase.CAMEL,
      'exclude': lambda x: not x
  }

  return field(default=default, default_factory=default_factory,
               **metadata(base=base, **kwargs))


def enum_field(default: Any = None, **kwargs) -> dataclasses.Field:
  base = {
      'encoder': lambda x: x.name if x else None
  }

  return standard_field(default=default, **base, **kwargs)


def list_field(default: Any = None, default_factory: Any = list,
               **kwargs) -> dataclasses.Field:
  base = {
      'encoder': lambda x: [
          f.render() if inspect.getmembers(
              f,
              lambda m: inspect.ismethod(m) and m.__name__ == 'render'
          ) else f.to_dict() for f in x],

  }

  return standard_field(default_factory=list, **base, **kwargs)


class AutoNumber(enum.Enum):
  def __repr__(self):
    return '<%s.%s>' % (self.__class__.__name__, self.name)

  def __new__(cls, *args, **kwargs):
    value = len(cls.__members__) + 1
    obj = object.__new__(cls)
    obj._value_ = value
    return obj
