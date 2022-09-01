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

from .color import Color


class ColorTest(unittest.TestCase):
  def test_valid_red(self) -> None:
    c = Color(red=1)
    self.assertDictEqual(
        c.to_dict(),
        {'red': 1})

  def test_valid_green(self) -> None:
    c = Color(green=0.5)
    self.assertDictEqual(
        c.to_dict(),
        {'green': 0.5})

  def test_valid_purple(self) -> None:
    c = Color(red=1, blue=0.5)
    self.assertDictEqual(
        c.to_dict(),
        {'red': 1, 'blue': 0.5})

  def test_invalid_number(self) -> None:
    with self.assertRaisesRegex(
            ValueError,
            'Color or alpha values must be between 0 and 1.'):
      c = Color(red=1.5)
