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

import unittest
from dataclasses import Field, dataclass
from typing import Callable, List

from dataclasses_json import dataclass_json

from card_framework import *
from card_framework.v2.action_response import ActionResponse
from card_framework.v2.action_status import ActionStatus


class TestEnum(enum.Enum):
  ONE = enum.auto()
  TWO = enum.auto()


class MetadataTest(unittest.TestCase):
  def test_simple_update(self) -> None:
    base = {'pirate': 'Westley'}

    updated = merge_metadata(base=base, pirate='Dread Pirate Roberts')

    self.assertDictEqual(updated, {'pirate': 'Dread Pirate Roberts'})

  def test_remove(self) -> None:
    base = {'pirate': 'Dread Pirate Roberts', 'swordsman': 'Inigo Montoya'}

    updated = merge_metadata(base=base, swordsman=None)

    self.assertDictEqual(updated, {'pirate': 'Dread Pirate Roberts'})

  def test_add(self) -> None:
    base = {'pirate': 'Dread Pirate Roberts', }

    updated = merge_metadata(base=base, swordsman='Inigo Montoya')

    self.assertDictEqual(updated, {'pirate': 'Dread Pirate Roberts',
                                   'swordsman': 'Inigo Montoya'})

  def test_add_and_remove(self) -> None:
    base = {'pirate': 'Dread Pirate Roberts', 'strongman': 'Fezzik'}

    updated = merge_metadata(
        base=base, swordsman='Inigo Montoya', strongman=None)

    self.assertDictEqual(updated, {'pirate': 'Dread Pirate Roberts',
                                   'swordsman': 'Inigo Montoya'})

  def test_add_update_and_remove(self) -> None:
    base = {'pirate': 'Westley', 'strongman': 'Fezzik'}

    updated = merge_metadata(base=base, swordsman='Inigo Montoya', strongman=None,
                             pirate='Dread Pirate Roberts')

    self.assertDictEqual(updated, {'pirate': 'Dread Pirate Roberts',
                                   'swordsman': 'Inigo Montoya'})


class StandardFieldTest(unittest.TestCase):
  def test_base_field(self) -> None:
    @dataclass_json
    @dataclass
    class Base(object):
      _field: str = standard_field()

    base = Base()
    base._field = 'foo'

    f: Field = base.__dataclass_fields__.get('_field')
    self.assertIsNone(f.default)
    self.assertTrue(isinstance(f.default_factory, dataclasses._MISSING_TYPE))
    self.assertIsNotNone(f.metadata)
    self.assertIn('letter_case', f.metadata['dataclasses_json'])
    self.assertIn('exclude', f.metadata['dataclasses_json'])

  def test_field_with_metadata_removed(self) -> None:
    @dataclass_json
    @dataclass
    class Base(object):
      _field: str = standard_field(exclude=None)

    base = Base()
    base._field = 'foo'

    f = base.__dataclass_fields__.get('_field')
    self.assertIsNone(f.default)
    self.assertTrue(isinstance(f.default_factory, dataclasses._MISSING_TYPE))
    self.assertIsNotNone(f.metadata)
    self.assertIn('letter_case', f.metadata['dataclasses_json'])
    self.assertNotIn('exclude', f.metadata['dataclasses_json'])

  def test_field_with_metadata_edited(self) -> None:
    @dataclass_json
    @dataclass
    class Base(object):
      _field: str = standard_field(exclude=True)

    base = Base()
    base._field = 'foo'

    f = base.__dataclass_fields__.get('_field')
    self.assertIsNone(f.default)
    self.assertTrue(isinstance(f.default_factory, dataclasses._MISSING_TYPE))
    self.assertIsNotNone(f.metadata)
    self.assertIn('letter_case', f.metadata['dataclasses_json'])
    self.assertTrue(f.metadata['dataclasses_json']['exclude'])

  def test_field_with_default(self) -> None:
    @dataclass_json
    @dataclass
    class Base(object):
      _field: str = standard_field(default='Princess Buttercup')

    base = Base()

    f = base.__dataclass_fields__.get('_field')
    self.assertIsNotNone(f.default)
    self.assertTrue(isinstance(f.default_factory, dataclasses._MISSING_TYPE))
    self.assertEqual(base._field, 'Princess Buttercup')


class EnumFieldTest(unittest.TestCase):
  class Fencer(AutoNumber):
    DREAD_PIRATE_ROBERTS = ()
    INIGO_MONTOYA = ()
    SIX_FINGERED_MAN = ()

  def test_base_field(self) -> None:
    @dataclass_json
    @dataclass
    class Base(object):
      _field: EnumFieldTest.Fencer = enum_field()

    base = Base()
    base._field = EnumFieldTest.Fencer.INIGO_MONTOYA

    f: Field = base.__dataclass_fields__.get('_field')
    self.assertIsNone(f.default)
    self.assertTrue(isinstance(f.default_factory, dataclasses._MISSING_TYPE))
    self.assertIsNotNone(f.metadata)
    self.assertIn('letter_case', f.metadata['dataclasses_json'])
    self.assertIn('exclude', f.metadata['dataclasses_json'])
    self.assertIn('encoder', f.metadata['dataclasses_json'])
    self.assertEqual(base._field, EnumFieldTest.Fencer.INIGO_MONTOYA)
    self.assertDictEqual(base.to_dict(), {'field': 'INIGO_MONTOYA'})

  def test_field_with_edited_encoder(self) -> None:
    @dataclass_json
    @dataclass
    class Base(object):
      _enum_field: EnumFieldTest.Fencer = enum_field(
          encoder=lambda x: x.value if x else None)

    base = Base()
    base._enum_field = EnumFieldTest.Fencer.SIX_FINGERED_MAN

    f: Field = base.__dataclass_fields__.get('_enum_field')
    print(EnumFieldTest.Fencer.SIX_FINGERED_MAN.value)
    print(ActionStatus.Code.ABORTED.value)
    self.assertIsNone(f.default)
    self.assertTrue(isinstance(f.default_factory, dataclasses._MISSING_TYPE))
    self.assertIsNotNone(f.metadata)
    self.assertIn('letter_case', f.metadata['dataclasses_json'])
    self.assertIn('exclude', f.metadata['dataclasses_json'])
    self.assertIn('encoder', f.metadata['dataclasses_json'])
    self.assertDictEqual(
        base.to_dict(),
        {'enumField': EnumFieldTest.Fencer.SIX_FINGERED_MAN.value})

  def test_field_with_metadata_removed(self) -> None:
    @dataclass_json
    @dataclass
    class Base(object):
      _enum_field: EnumFieldTest.Fencer = enum_field(letter_case=None)

    base = Base()
    base._enum_field = EnumFieldTest.Fencer.SIX_FINGERED_MAN

    f: Field = base.__dataclass_fields__.get('_enum_field')
    self.assertIsNotNone(f.metadata)
    self.assertNotIn('letter_case', f.metadata['dataclasses_json'])
    self.assertDictEqual(
        base.to_dict(),
        {'_enum_field': EnumFieldTest.Fencer.SIX_FINGERED_MAN.name})


class ListFieldTest(unittest.TestCase):
  def test_base_list_field_str(self) -> None:
    @dataclass_json
    @dataclass
    class Base(object):
      _list_field: List[str] = list_field()

    base = Base()
    base._list_field = 'Hello, my name is Inigo Montoya'.split(' ')

    f: Field = base.__dataclass_fields__.get('_list_field')
    self.assertEqual(f.default_factory, list)
    self.assertTrue(isinstance(f.default, dataclasses._MISSING_TYPE))
    self.assertIsNotNone(f.metadata)
    self.assertIn('letter_case', f.metadata['dataclasses_json'])
    self.assertIn('exclude', f.metadata['dataclasses_json'])
    self.assertIn('encoder', f.metadata['dataclasses_json'])
    self.assertListEqual(
        'Hello, my name is Inigo Montoya'.split(' '), base._list_field)
    self.assertDictEqual(
        base.to_dict(),
        {'listField': ['Hello,', 'my', 'name', 'is', 'Inigo', 'Montoya']})

  def test_base_list_field_int(self) -> None:
    @dataclass_json
    @dataclass
    class Base(object):
      _list_field: List[int] = list_field()

    base = Base()
    base._list_field = [1, 2, 3, 4, 5, ]

    f: Field = base.__dataclass_fields__.get('_list_field')
    self.assertEqual(f.default_factory, list)
    self.assertTrue(isinstance(f.default, dataclasses._MISSING_TYPE))
    self.assertIsNotNone(f.metadata)
    self.assertIn('letter_case', f.metadata['dataclasses_json'])
    self.assertIn('exclude', f.metadata['dataclasses_json'])
    self.assertIn('encoder', f.metadata['dataclasses_json'])
    self.assertListEqual(
        [1, 2, 3, 4, 5, ], base._list_field)
    self.assertDictEqual(
        base.to_dict(),
        {'listField': [1, 2, 3, 4, 5]})

  def test_base_list_field_no_render(self) -> None:
    @dataclass_json
    @dataclass
    class Base(object):
      _list_field: List[ActionStatus] = list_field()

    LIST_UNDER_TEST = [
        ActionStatus(status_code=ActionStatus.Code.OK,
                     user_facing_message='Hello, my name is Inigo Montoya'),
        ActionStatus(status_code=ActionStatus.Code.UNKNOWN,
                     user_facing_message='Inconcievable!'),
    ]
    base = Base()
    base._list_field = LIST_UNDER_TEST

    f: Field = base.__dataclass_fields__.get('_list_field')
    self.assertEqual(f.default_factory, list)
    self.assertTrue(isinstance(f.default, dataclasses._MISSING_TYPE))
    self.assertIsNotNone(f.metadata)
    self.assertIn('letter_case', f.metadata['dataclasses_json'])
    self.assertIn('exclude', f.metadata['dataclasses_json'])
    self.assertIn('encoder', f.metadata['dataclasses_json'])
    self.assertListEqual(
        LIST_UNDER_TEST, base._list_field)

    self.assertDictEqual(
        base.to_dict(),
        {'listField': [{'statusCode': 'OK',
                        'userFacingMessage': 'Hello, my name is Inigo Montoya'},
                       {'statusCode': 'UNKNOWN',
                        'userFacingMessage': 'Inconcievable!'}]})

  def test_base_list_field_render(self) -> None:
    """test_base_list_field_render

    ActionResponse has a render method, which causes the tag 'actionResponse' to
    be the root of each rendered element unlike a `to_dict` call which would
    drop the camel-cased class name.
    """
    @dataclass_json
    @dataclass
    class Base(object):
      _list_field: List[ActionResponse] = list_field()

    LIST_UNDER_TEST = [
        ActionResponse(
            type=ActionResponse.ResponseType.NEW_MESSAGE,
            url='http://www.karentaylorart.com'
        ),
        ActionResponse(
            type=ActionResponse.ResponseType.NEW_MESSAGE,
            url='http://www.imdb.com/title/tt0093779/'
        ),
    ]
    base = Base()
    base._list_field = LIST_UNDER_TEST

    f: Field = base.__dataclass_fields__.get('_list_field')
    self.assertEqual(f.default_factory, list)
    self.assertTrue(isinstance(f.default, dataclasses._MISSING_TYPE))
    self.assertIsNotNone(f.metadata)
    self.assertIn('letter_case', f.metadata['dataclasses_json'])
    self.assertIn('exclude', f.metadata['dataclasses_json'])
    self.assertIn('encoder', f.metadata['dataclasses_json'])
    self.assertListEqual(
        LIST_UNDER_TEST, base._list_field)

    self.assertDictEqual(
        base.to_dict(),
        {'listField': [
            {'actionResponse': {'type': 'NEW_MESSAGE',
                                'url': 'http://www.karentaylorart.com'}},
            {'actionResponse': {'type': 'NEW_MESSAGE',
                                'url': 'http://www.imdb.com/title/tt0093779/'}}
        ]})

  def test_list_with_thing_with_render_property(self) -> None:
    @dataclass_json
    @dataclass
    class Thing(object):
      render: str = standard_field()

    @dataclass_json
    @dataclass
    class Base(object):
      _list_field: List[Thing] = list_field()

    LIST_UNDER_TEST = [
        Thing(render='Florin'),
        Thing(render='Guilder')
    ]
    base = Base()
    base._list_field = LIST_UNDER_TEST

    print(Thing(render='Florin').to_dict())
    f: Field = base.__dataclass_fields__.get('_list_field')
    self.assertEqual(f.default_factory, list)
    self.assertTrue(isinstance(f.default, dataclasses._MISSING_TYPE))
    self.assertIsNotNone(f.metadata)
    self.assertIn('letter_case', f.metadata['dataclasses_json'])
    self.assertIn('exclude', f.metadata['dataclasses_json'])
    self.assertIn('encoder', f.metadata['dataclasses_json'])
    self.assertListEqual(
        LIST_UNDER_TEST, base._list_field)

    self.assertDictEqual(
        base.to_dict(),
        {'listField': [
            {'render': 'Florin'},
            {'render': 'Guilder'},
        ]})


class RenderableTest(unittest.TestCase):
  def test_render(self) -> None:
    @dataclass_json
    @dataclass
    class Base(Renderable):
      _field: str = standard_field()

    base = Base(_field='Hello, my name is Inigo Montoya.')

    self.assertDictEqual(
        base.render(),
        {'base': {'field': 'Hello, my name is Inigo Montoya.'}})

  def test_render_no_tag_name(self) -> None:
    @dataclass_json
    @dataclass
    class Base(Renderable):
      __SUPPRESS_TAG__ = True
      _field: str = standard_field()

    base = Base(_field='Hello, my name is Inigo Montoya.')

    self.assertDictEqual(
        base.render(),
        {'field': 'Hello, my name is Inigo Montoya.'})

  def test_render_tag_override(self) -> None:
    @dataclass_json
    @dataclass
    class Base(Renderable):
      __OVERRIDE_TAG__ = 'overriddenTagName'
      _field: str = standard_field()

    base = Base(_field='Hello, my name is Inigo Montoya.')

    self.assertDictEqual(
        base.render(),
        {'overriddenTagName': {'field': 'Hello, my name is Inigo Montoya.'}})
