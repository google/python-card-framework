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
from .enums import ImageType


class HeaderTest(unittest.TestCase):
  def test_full_header(self) -> None:
    h = CardHeader(
        title='The Princess Bride',
        subtitle=("There's a shortage of perfect movies in this world. "
                  "It would be a pity to damage this one."),
        image_url='https://en.wikipedia.org/wiki/File:Princess_bride.jpg',
        image_alt_text="It's as real as the feelings you feel.",
        image_type=ImageType.CIRCLE)

    self.assertDictEqual(
        h.to_dict(),
        {
            'imageType': 'CIRCLE',
            'imageAltText': "It's as real as the feelings you feel.",
            'imageUrl': 'https://en.wikipedia.org/wiki/File:Princess_bride.jpg',
            'subtitle': "There's a shortage of perfect movies in this world. "
                        "It would be a pity to damage this one.",
            'title': 'The Princess Bride'})

  def test_header_no_image(self) -> None:
    h = CardHeader(
        title='The Princess Bride',
        subtitle=("There's a shortage of perfect movies in this world. "
                  "It would be a pity to damage this one."))

    self.assertDictEqual(h.to_dict(),
                         {'subtitle': "There's a shortage of perfect movies in this world. It would be "
                          'a pity to damage this one.',
                          'title': 'The Princess Bride',
                          })

  def test_header_no_subtitle(self) -> None:
    h = CardHeader(title='The Princess Bride')

    self.assertDictEqual(h.to_dict(),
                         {'title': 'The Princess Bride', })

  def test_header_image_no_style(self) -> None:
    h = CardHeader(
        title='The Princess Bride',
        image_url='https://en.wikipedia.org/wiki/File:Princess_bride.jpg',
        subtitle=("There's a shortage of perfect movies in this world. "
                  "It would be a pity to damage this one."))

    with self.assertRaises(ValueError):
      h.to_dict()
