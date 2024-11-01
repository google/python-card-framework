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

from ..enums import HorizontalAlignment
from .chip_list import Chip, ChipList
from .icon import Icon
from .on_click import OnClick
from .open_link import OpenLink


class ChipListTest(unittest.TestCase):
  chip = Chip(label='Inconceivable!', on_click=OnClick(
      open_link=OpenLink(url='https://www.karentaylorart.com')))

  def test_multiple_chips(self) -> None:
    t = ChipList()
    t.chips.append(self.chip)
    t.chips.append(self.chip)
    t.chips.append(self.chip)

    self.assertDictEqual(
        t.to_dict(),
        {'chips':
            [
                {'onClick': {'openLink': {'url': 'https://www.karentaylorart.com'}},
                 'label': 'Inconceivable!'},
                {'onClick': {'openLink': {'url': 'https://www.karentaylorart.com'}},
                 'label': 'Inconceivable!'},
                {'onClick': {'openLink': {'url': 'https://www.karentaylorart.com'}},
                 'label': 'Inconceivable!'},
            ]}
    )


class ChipTest(unittest.TestCase):
  def test_label_chip(self) -> None:
    label = 'Inconceivable!'
    on_click = OnClick(open_link=OpenLink(url='https://www.karentaylorart.com'))
    t = Chip(label=label, on_click=on_click)

    self.assertDictEqual(
        t.to_dict(),
        {
            'onClick': {'openLink': {'url': 'https://www.karentaylorart.com'}},
            'label': 'Inconceivable!'}
    )

  def test_icon_chip(self) -> None:
    i = Chip(on_click=OnClick(open_link='http://www.karentaylorart.com'))
    i.icon = Icon(known_icon=Icon.KnownIcon.AIRPLANE)
    self.assertDictEqual(
        i.to_dict(),
        {
            'icon': {
                'knownIcon': 'AIRPLANE'},
            'onClick': {'openLink': 'http://www.karentaylorart.com'},
        }
    )

  def test_icon_url_chip(self) -> None:
    self.maxDiff = None
    i = Chip(on_click=OnClick(open_link='http://www.karentaylorart.com'))
    i.icon = Icon(
        icon_url='https://www.karentaylorart.com/wp-content/uploads/2021/01/go_small.jpg')
    self.assertDictEqual(
        i.to_dict(),
        {
            'icon': {
                'iconUrl': 'https://www.karentaylorart.com/wp-content/uploads/2021/01/go_small.jpg',
            },
            'onClick': {'openLink': 'http://www.karentaylorart.com'},
        })

  def test_aligned_label_chip(self) -> None:
    label = 'Inconceivable!'
    on_click = OnClick(open_link=OpenLink(url='https://www.karentaylorart.com'))
    t = Chip(label=label, on_click=on_click)
    t.horizontal_alignment = HorizontalAlignment.CENTER

    self.assertDictEqual(
        t.to_dict(),
        {
            'onClick': {
                'openLink': {
                    'url': 'https://www.karentaylorart.com'}
            },
            'label': 'Inconceivable!'}
    )

  def test_disabled_label_chip(self) -> None:
    label = 'Inconceivable!'
    on_click = OnClick(open_link=OpenLink(url='https://www.karentaylorart.com'))
    t = Chip(label=label, on_click=on_click, disabled=True)
    t.horizontal_alignment = HorizontalAlignment.CENTER

    self.assertDictEqual(
        t.to_dict(),
        {
            'onClick': {
                'openLink': {
                    'url': 'https://www.karentaylorart.com'}
            },
            'label': 'Inconceivable!',
            'disabled': True}
    )
