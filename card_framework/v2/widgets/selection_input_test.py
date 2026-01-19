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

from card_framework.v2.widgets.action import Action, ActionParameter
from card_framework.v2.widgets.selection_input import SelectionInput
from card_framework.v2.widgets.selection_item import SelectionItem, SelectionItems


class SelectionInputTest(unittest.TestCase):
  def test_simple_render(self) -> None:
    self.assertDictEqual(SelectionInput(name='Inigo Montoya').render(),
                         {'selectionInput': {'name': 'Inigo Montoya'}})

  def test_render_complete(self) -> None:
    self.maxDiff = None
    items = [
        SelectionItem(text='left hand', value='l', selected=True),
        SelectionItem(text='right hand', value='r'),
    ]

    i = SelectionInput()
    i.name = 'inigo'
    i.label = 'Inigo Montoya'
    i.type = SelectionInput.SelectionType.DROPDOWN
    i.items = items
    i.on_change_action = Action(function='switch_hand', parameters=[
        ActionParameter(key='Over too quick', value='left'),
        ActionParameter(key='Not left handed', value='right')])

    self.assertDictEqual(i.render(),
                         {'selectionInput': {
                          'name': 'inigo',
                          'label': 'Inigo Montoya',
                          'type': 'DROPDOWN',
                          'items': [
                                  {'text': 'left hand',
                                   'value': 'l', 'selected': True},
                                  {'text': 'right hand', 'value': 'r'}
                          ],
                          'onChangeAction': {
                              'function': 'switch_hand',
                              'parameters': [
                                  {'key': 'Over too quick', 'value': 'left'},
                                  {'key': 'Not left handed', 'value': 'right'}
                              ]}}}
                         )
