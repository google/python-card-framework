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

import unittest

from card_framework import *
from dataclasses import dataclass
from typing import Any, List, Mapping

from card_framework import list_field, standard_field
from dataclasses_json import dataclass_json, LetterCase


class LazyPropertyTest(unittest.TestCase):
  class Foo(object):
    @lazy_property
    def lazy_thing(self) -> str:
      return 'lazy'

  def test_lazy_thing(self):
    foo = LazyPropertyTest.Foo()
    self.assertFalse(hasattr(foo, '_lazy_lazy_thing'))
    self.assertEqual('lazy', foo.lazy_thing)
    self.assertTrue(hasattr(foo, '_lazy_lazy_thing'))


class TestEnum(AutoNumber):
  ONE = 'ONE'
  TWO = 'TWO'


class EnumFieldTest(unittest.TestCase):
  @dataclass_json
  @dataclass
  class TestClass(object):
    field_enum: TestEnum = enum_field()

  def test_no_default(self) -> None:
    field = enum_field()

    self.assertIsNone(field.default)

  def test_default(self) -> None:
    field = enum_field(TestEnum.ONE)

    self.assertEqual(field.default, TestEnum.ONE)

  def test_class_render_empty(self) -> None:
    c = self.TestClass()

    self.assertDictEqual(c.to_dict(), {})

  def test_class_render_populated(self) -> None:
    c = self.TestClass()
    c.field_enum = TestEnum.ONE

    self.assertDictEqual(c.to_dict(), {'fieldEnum': 'ONE'})

  def test_class_render_change_case(self) -> None:
    @dataclass_json
    @dataclass
    class ToTest(object):
      field_enum: TestEnum = enum_field(default=TestEnum.ONE,
                                        letter_case=LetterCase.SNAKE)
    c = ToTest()

    self.assertDictEqual(c.to_dict(), {'field_enum': 'ONE'})

  def test_class_render_change_name(self) -> None:
    @dataclass_json
    @dataclass
    class ToTest(object):
      field_enum: TestEnum = enum_field(default=TestEnum.ONE,
                                        field_name='foo')
    c = ToTest()

    self.assertDictEqual(c.to_dict(), {'foo': 'ONE'})


class MetadataTest(unittest.TestCase):
  def test_simple_update(self) -> None:
    base = {'pirate': 'Westley'}

    updated = metadata(base=base, pirate='Dread Pirate Roberts')

    self.assertDictEqual(updated, {'pirate': 'Dread Pirate Roberts'})

  def test_remove(self) -> None:
    base = {'pirate': 'Dread Pirate Roberts', 'swordsman': 'Inigo Montoya'}

    updated = metadata(base=base, swordsman=None)

    self.assertDictEqual(updated, {'pirate': 'Dread Pirate Roberts'})

  def test_add(self) -> None:
    base = {'pirate': 'Dread Pirate Roberts', }

    updated = metadata(base=base, swordsman='Inigo Montoya')

    self.assertDictEqual(updated, {'pirate': 'Dread Pirate Roberts',
                                   'swordsman': 'Inigo Montoya'})

  def test_add_and_remove(self) -> None:
    base = {'pirate': 'Dread Pirate Roberts', 'strongman': 'Fezzik'}

    updated = metadata(base=base, swordsman='Inigo Montoya', strongman=None)

    self.assertDictEqual(updated, {'pirate': 'Dread Pirate Roberts',
                                   'swordsman': 'Inigo Montoya'})

  def test_add_update_and_remove(self) -> None:
    base = {'pirate': 'Westley', 'strongman': 'Fezzik'}

    updated = metadata(base=base, swordsman='Inigo Montoya', strongman=None,
                       pirate='Dread Pirate Roberts')

    self.assertDictEqual(updated, {'pirate': 'Dread Pirate Roberts',
                                   'swordsman': 'Inigo Montoya'})
