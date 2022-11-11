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
from .card_header import CardHeader
from .card import Card
from .section import Section
from .widgets.text_paragraph import TextParagraph


class CardTest(unittest.TestCase):
  def test_simple_render(self) -> None:
    self.maxDiff = None
    header = CardHeader(title='Princess Bride')
    section = Section()
    section.add_widget(TextParagraph(text="Inconceivable!"))
    card = Card()
    card.card_id = 'vizzini'
    card.header = header
    card.add_section(section)
    output = card.render()

    self.assertDictEqual(
        output,
        {
            'cardId': 'vizzini',
            'card': {
                'header': {'title': 'Princess Bride'},
                'sections': [{
                    'widgets': [
                      {'textParagraph': {
                          'text': 'Inconceivable!'
                      }}]}]}})

  def test_render_no_header(self) -> None:
    self.maxDiff = None
    section = Section()
    section.add_widget(TextParagraph(text="Inconceivable!"))
    card = Card()
    card.card_id = 'vizzini'
    card.add_section(section)
    output = card.render()

    self.assertDictEqual(
        output,
        {
            'cardId': 'vizzini',
            'card': {
                'sections': [{
                    'widgets': [
                      {'textParagraph': {
                          'text': 'Inconceivable!'
                      }}]}]}})

  def test_render_default_card_id(self) -> None:
    self.maxDiff = None
    section = Section()
    section.add_widget(TextParagraph(text="Inconceivable!"))
    card = Card()
    card.add_section(section)
    output = card.render()

    self.assertTrue('cardId' in output)
    self.assertIsNotNone(output['cardId'])
