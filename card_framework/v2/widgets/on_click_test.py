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

from .action import Action, ActionParameter
from .on_click import OnClick
from .open_link import OpenLink


class OnClickTest(unittest.TestCase):
  def test_on_click_empty(self) -> None:
    o = OnClick()
    self.assertEqual(o.action, None)
    self.assertEqual(o.open_link, None)
    self.assertEqual({}, o.to_dict())

  def test_on_click_action(self) -> None:
    o = OnClick()
    o.action = Action(function='method', parameters=[
        ActionParameter(key='key1', value='value1'),
        ActionParameter(key='key2', value='value2'),
    ])
    self.assertNotEqual(o.action, None)
    self.assertEqual(o.open_link, None)
    self.assertEqual({'action': {'function': 'method',
                                 'parameters': [
                                     {'key': 'key1', 'value': 'value1'},
                                     {'key': 'key2', 'value': 'value2'}]}},
                     o.to_dict())

  def test_on_click_open_link(self) -> None:
    o = OnClick()
    o.open_link = OpenLink(url='https://www.karentaylorart.com')
    self.assertEqual(o.action, None)
    self.assertNotEqual(o.open_link, None)
    self.assertEqual({'openLink': {'url': 'https://www.karentaylorart.com'}},
                     o.to_dict())

  def test_on_click_action_after_open_link(self) -> None:
    o = OnClick()
    o.open_link = OpenLink(url='https://www.karentaylorart.com')

    self.assertEqual(o.action, None)
    self.assertNotEqual(o.open_link, None)

    o.action = Action(function='method', parameters=[
        ActionParameter(key='key1', value='value1'),
        ActionParameter(key='key2', value='value2'),
    ])

    self.assertNotEqual(o.action, None)
    self.assertEqual(o.open_link, None)
    self.assertEqual({'action': {'function': 'method',
                                 'parameters': [
                                     {'key': 'key1', 'value': 'value1'},
                                     {'key': 'key2', 'value': 'value2'}]}},
                     o.to_dict())

  def test_on_click_open_link_after_action(self) -> None:
    o = OnClick()
    o.action = Action(function='method', parameters=[
        ActionParameter(key='key1', value='value1'),
        ActionParameter(key='key2', value='value2'),
    ])

    self.assertNotEqual(o.action, None)
    self.assertEqual(o.open_link, None)

    o.open_link = OpenLink(url='https://www.karentaylorart.com')

    self.assertEqual(o.action, None)
    self.assertNotEqual(o.open_link, None)
    self.assertEqual({'openLink': {'url': 'https://www.karentaylorart.com'}},
                     o.to_dict())
