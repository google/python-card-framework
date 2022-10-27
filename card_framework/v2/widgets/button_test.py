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
from .button import Button
from .icon import Icon
from .on_click import OnClick
from .open_link import OpenLink


class ButtonTest(unittest.TestCase):
  def test_text_button(self) -> None:
    text = 'Inconceivable!'
    on_click = OnClick(open_link=OpenLink(url='https://www.karentaylorart.com'))
    t = Button(text=text, on_click=on_click)

    self.assertDictEqual(
        t.to_dict(),
        {
            'onClick': {'openLink': {'url': 'https://www.karentaylorart.com'}},
            'text': 'Inconceivable!'}
    )

  def test_icon_button(self) -> None:
    i = Button(on_click=OnClick(open_link='http://www.karentaylorart.com'))
    i.icon = Icon(known_icon=Icon.KnownIcon.AIRPLANE)
    self.assertDictEqual(
        i.to_dict(),
        {
            'icon': {
                'knownIcon': 'AIRPLANE'},
            'onClick': {'openLink': 'http://www.karentaylorart.com'},
        }
    )

  def test_icon_url_button(self) -> None:
    self.maxDiff = None
    i = Button(on_click=OnClick(open_link='http://www.karentaylorart.com'))
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

  def test_aliugned_text_button(self) -> None:
    text = 'Inconceivable!'
    on_click = OnClick(open_link=OpenLink(url='https://www.karentaylorart.com'))
    t = Button(text=text, on_click=on_click)
    t.horizontal_alignment = HorizontalAlignment.CENTER

    self.assertDictEqual(
        t.to_dict(),
        {
            'onClick': {
                'openLink': {
                    'url': 'https://www.karentaylorart.com'}
            },
            'text': 'Inconceivable!'}
    )
