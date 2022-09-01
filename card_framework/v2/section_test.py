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

from dataclasses import dataclass
import unittest

from dataclasses_json import LetterCase, dataclass_json

from .enums import HorizontalAlignment

from .section import Section
from .widget import Widget


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TestWidget(Widget):
  """Good Widget"""
  text: str = ''

  @property
  def _widget_tag(self) -> str:
    return 'testWidget'


class SectionTest(unittest.TestCase):
  def test_empty(self) -> None:
    section = Section()

    self.assertEqual(list(), section.widgets)
    self.assertEqual(None, section.header)
    self.assertDictEqual(
        section.to_dict(),
        {})

  def test_fully_specified(self) -> None:
    header = 'Princess Bride'
    widget = TestWidget(text="You keep using that word...")

    section = Section()
    section.header = header
    section.add_widget(widget)

    self.assertEqual(1, len(section.widgets))
    self.assertEqual({
        'header': 'Princess Bride',
        'widgets': [{
            'testWidget': {'text': 'You keep using that word...'}}, ],
    },
        section.to_dict())

  def test_header_no_widgets(self) -> None:
    header = 'Princess Bride'

    section = Section()
    section.header = header
    self.assertEqual(list(), section.widgets)
    self.assertEqual({
        'header': 'Princess Bride',
    }, section.to_dict())

  def test_widgets_no_header(self) -> None:
    widget = TestWidget(text="You keep using that word...")

    section = Section()
    section.add_widget(widget)

    self.assertEqual(1, len(section.widgets))
    self.assertDictEqual(section.to_dict(),
                         {
        'widgets': [{
            'testWidget': {'text': 'You keep using that word...'}}, ], }
    )

  def test_multiple_widgets(self) -> None:
    header = 'Princess Bride'
    section = Section()
    section.header = header
    section.add_widget(TestWidget(text="You keep using that word..."))
    section.add_widget(TestWidget(text="Inconceivable!"))

    self.assertEqual(2, len(section.widgets))
    self.assertEqual({
        'header': 'Princess Bride',
        'widgets': [{
            'testWidget': {'text': 'You keep using that word...'}}, {
            'testWidget': {'text': 'Inconceivable!'}}],
    },
        section.to_dict())

  def test_aligned_widget(self) -> None:
    widget = TestWidget(text="You keep using that word...")
    widget.horizontal_alignment = HorizontalAlignment.CENTER
    widget.to_dict()

    section = Section()
    section.add_widget(widget)

    self.assertEqual(1, len(section.widgets))
    self.assertDictEqual({
        'widgets': [{
            'horizontalAlignment': 'CENTER',
            'testWidget': {'text': 'You keep using that word...'}}, ],
    },
        section.to_dict())
