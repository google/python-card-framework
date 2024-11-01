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

from .icon import Icon


class IconTest(unittest.TestCase):
  def test_icon_icon_url(self) -> None:
    i = Icon(
        icon_url='https://www.karentaylorart.com/wp-content/uploads/2021/01/go_small.jpg')

    self.assertDictEqual(
        i.to_dict(),
        {
            'iconUrl': 'https://www.karentaylorart.com/wp-content/uploads/2021/01/go_small.jpg',
        })

  def test_icon_to_url(self) -> None:
    i = Icon(
        icon_url='https://www.karentaylorart.com/wp-content/uploads/2021/01/go_small.jpg')
    self.assertIsNone(i.known_icon)

    i.known_icon = Icon.KnownIcon.AIRPLANE
    self.assertIsNone(i.icon_url)
    self.assertEqual(
        i.to_dict(),
        {

            'knownIcon': 'AIRPLANE',
        })

  def test_url_to_icon(self) -> None:
    i = Icon(known_icon=Icon.KnownIcon.AIRPLANE)
    self.assertIsNone(i.icon_url)

    i.icon_url = 'https://www.karentaylorart.com/wp-content/uploads/2021/01/go_small.jpg'
    self.assertIsNone(i.known_icon)
    self.assertEqual(
        i.to_dict(),
        {
            'iconUrl': 'https://www.karentaylorart.com/wp-content/uploads/2021/01/go_small.jpg',
        })

  def test_must_have_one(self) -> None:
    i = Icon()

    with self.assertRaisesRegex(ValueError, 'One of .* must be set\.'):
      i.to_dict()

  def test_material_icon(self) -> None:
    i = Icon(material_icon=Icon.MaterialIcon(name='home'))

    self.assertIsNone(i.icon_url)
    self.assertEqual(
        i.to_dict(),
        {
            'materialIcon': {'name': 'home'},
        })
