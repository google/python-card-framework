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

from .text_paragraph import TextParagraph


class TextParagraphTest(unittest.TestCase):
  def test_simple_render(self) -> None:
    self.assertDictEqual(TextParagraph(text='Foo!').render(),
                         {'text_paragraph': {'text': 'Foo!'}})

  def test_aligned(self) -> None:
    text_paragraph = TextParagraph(text='Foo!')
    text_paragraph.horizontal_alignment = HorizontalAlignment.CENTER

    print(text_paragraph.render())

    self.assertDictEqual(text_paragraph.render(),
                         {'text_paragraph': {'text': 'Foo!'},
                          'horizontal_alignment': 'CENTER'})
