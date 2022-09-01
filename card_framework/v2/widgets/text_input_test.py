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
from card_framework.v2.widgets.suggestions import SuggestionItem, Suggestions

from .text_input import TextInput


class TextInputTest(unittest.TestCase):
  def test_simple_render(self) -> None:
    self.assertDictEqual(TextInput(name='Inigo Montoya').render(),
                         {'textInput': {'name': 'Inigo Montoya'}})

  def test_render_complete(self) -> None:
    self.maxDiff = None
    i = TextInput()
    i.name = 'inigo'
    i.hint_text = 'You killed my father.'
    i.initial_suggestions = Suggestions(
        [SuggestionItem(text='Prepare to die.')]
    )
    i.label = 'Inigo Montoya'
    i.value = 'Anything you want.'
    i.auto_complete_action = Action(function='duel')
    i.on_change_action = Action(function='switch_hand', parameters=[
        ActionParameter(key='Over too quick', value='left'),
        ActionParameter(key='Not left handed', value='right')])

    print(i.render())

    self.assertDictEqual(i.render(),
                         {'textInput': {'name': 'inigo',
                                        'label': 'Inigo Montoya',
                                        'hintText': 'You killed my father.',
                                        'onChangeAction': {
                                            'function': 'switch_hand',
                                            'parameters': [
                                                {'key': 'Over too quick',
                                                 'value': 'left'},
                                                {'key': 'Not left handed',
                                                 'value': 'right'}
                                            ]},
                                        'value': 'Anything you want.',
                                        'initialSuggestions': {
                                            'items': [
                                                {'text': 'Prepare to die.'}
                                            ]},
                                        'autoCompleteAction': {
                                            'function': 'duel',
                                        }}}
                         )
