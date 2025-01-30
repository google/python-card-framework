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
from typing import List

from dataclasses_json import dataclass_json

from . import *
from .message import Message
from .card_header import CardHeader
from .card import Card, CardWithId
from .section import Section
from .widgets.text_paragraph import TextParagraph


class MessageTest(unittest.TestCase):
  def test_empty_message(self) -> None:
    m = Message()
    m.name = 'Inigo Montoya'

    self.assertDictEqual(m.render(), {'name': 'Inigo Montoya'})

  def test_cardsV2_message(self) -> None:
    self.maxDiff = None

    m = Message()
    m.name = 'Inigo Montoya'
    header = CardHeader(title='Princess Bride')
    section = Section()
    section.add_widget(TextParagraph(text="Inconceivable!"))
    card = CardWithId()
    card.card_id = 'vizzini'
    card.header = header
    card.add_section(section)
    m.cards_v2.append(card)
    output = m.render()
    print(output)

    self.assertDictEqual(
        output,
        {
            'name': 'Inigo Montoya',
            'cards_v2': [{
                'card': {
                    'header': {'title': 'Princess Bride'},
                    'sections': [
                        {'widgets': [
                            {'text_paragraph': {'text': 'Inconceivable!'}}
                        ]}
                    ]},
                'card_id': 'vizzini'}
            ]})
