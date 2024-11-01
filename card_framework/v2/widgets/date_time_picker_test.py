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

from card_framework.v2.widgets.action import Action

from .date_time_picker import DateTimePicker


class DateTimePickerTest(unittest.TestCase):
  maxDiff = None

  def test_date_time_picker(self) -> None:
    name = 'Now'
    label = 'A date time picker'
    type_ = DateTimePicker.Type.DATE_AND_TIME
    on_change_action = Action(function='do_this')

    t = DateTimePicker(name=name, type_=type_, label=label,
                       on_change_action=on_change_action)

    self.assertDictEqual(
        t.to_dict(),
        {'label': 'A date time picker',
            'name': 'Now',
            'onChangeAction': {'function': 'do_this'},
            'type': 'DATE_AND_TIME'})

  def test_date_only_picker(self) -> None:
    name = 'Now'
    type_ = DateTimePicker.Type.DATE_ONLY
    on_change_action = Action(function='do_this')

    t = DateTimePicker(name=name, type_=type_,
                       on_change_action=on_change_action)

    self.assertDictEqual(
        t.to_dict(),
        {'name': 'Now',
         'onChangeAction': {'function': 'do_this'},
         'type': 'DATE_ONLY'})

  def test_time_only_picker(self) -> None:
    name = 'Now'
    type_ = DateTimePicker.Type.TIME_ONLY
    on_change_action = Action(function='do_this')

    t = DateTimePicker(name=name, type_=type_,
                       on_change_action=on_change_action)

    self.assertDictEqual(
        t.to_dict(),
        {'name': 'Now',
         'onChangeAction': {'function': 'do_this'},
         'type': 'TIME_ONLY'})
