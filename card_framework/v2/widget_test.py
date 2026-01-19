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
from dataclasses import dataclass
from typing import List

from dataclasses_json import LetterCase, dataclass_json
from card_framework import standard_field

from card_framework.v2.enums import HorizontalAlignment

from .widget import Widget


@dataclass_json
@dataclass
class ValidWidget(Widget):
  """Good Widget"""
  camel_case_property: str = standard_field()


class WidgetTest(unittest.TestCase):

  def test_valid_widget_render(self) -> None:
    widget = ValidWidget()
    widget.camel_case_property = 'Inigo Montoya'
    self.assertDictEqual(
        widget.render(),
        {'validWidget': {'camelCaseProperty': 'Inigo Montoya'}})

  def test_aligned_widget_render(self) -> None:
    widget = ValidWidget()
    widget.camel_case_property = 'Inigo Montoya'
    widget.horizontal_alignment = HorizontalAlignment.END
    self.assertDictEqual(
        widget.render(),
        {'horizontalAlignment': 'END',
         'validWidget': {'camelCaseProperty': 'Inigo Montoya'}})
