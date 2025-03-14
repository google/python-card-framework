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


from card_framework.v2.action_response import ActionResponse
from card_framework.v2.widgets.selection_input import UpdatedWidget
from card_framework.v2.widgets.selection_item import SelectionItem, SelectionItems
from card_framework.v2.dialog_action import DialogAction
from card_framework.v2.user import User


class ActionResponseTest(unittest.TestCase):
  def test_render_action_response(self) -> None:
    items = SelectionItems()
    items.items = [
        SelectionItem(text='left hand', value='l', selected=True),
        SelectionItem(text='right hand', value='r'),
    ]

    a = ActionResponse(type=ActionResponse.ResponseType.DIALOG)
    a.url = 'www.karentaylorart.com'
    a.dialog_action = DialogAction()
    a.updated_widget = UpdatedWidget(widget='inigo', suggestions=items)

    print(a.render())

    self.assertDictEqual(
        a.render(),
        {'action_response': {
            'type': 'DIALOG',
            'url': 'www.karentaylorart.com',
            'updated_widget': {
                'widget': 'inigo',
                'suggestions': {
                    'items': [
                        {'selection_item': {
                          'text': 'left hand',
                          'value': 'l',
                          'selected': True}},
                        {'selection_item': {
                            'text': 'right hand',
                            'value': 'r'}}]}}}}
    )
