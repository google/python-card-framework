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

from .decorated_text import DecoratedText

from .columns import Columns, Column


class ColumnsTest(unittest.TestCase):
  maxDiff = None

  def test_two_columns(self) -> None:
    c1 = Column(horizontal_alignment=Column.HorizontalAlignment.START,
                widgets=[DecoratedText(
                    text="You are using Bonetti's defense against me!")])
    c2 = Column(horizontal_alignment=Column.HorizontalAlignment.END,
                widgets=[DecoratedText(
                    text="I thought it fitting considering the rocky terrain.")])
    c = Columns(column_items=[c1, c2,])

    self.assertDictEqual(
        c.to_dict(),
        {'columnItems': [{'horizontalAlignment': 'START',
                          'widgets': [{'decoratedText': {'text': 'You are using '
                                                         "Bonetti's defense "
                                                         'against me!'}}]},
                         {'horizontalAlignment': 'END',
                          'widgets': [{'decoratedText': {'text': 'I thought it fitting '
                                                         'considering the '
                                                         'rocky terrain.'}}]}]}
    )

  def test_two_columns_multiple_widgets(self) -> None:
    c1 = Column(horizontal_alignment=Column.HorizontalAlignment.START,
                widgets=[
                    DecoratedText(
                        text="You are using Bonetti's defense against me!"),
                    DecoratedText(
                        text="You must expect me to respond with Capaferro."),
                ])
    c2 = Column(horizontal_alignment=Column.HorizontalAlignment.END,
                widgets=[
                    DecoratedText(
                        text="I thought it fitting considering the rocky terrain."),
                    DecoratedText(
                        text="Natually, but I find Tybalt cancels out Capaferro, don't you?"),
                ])
    c = Columns(column_items=[c1, c2,])

    self.assertDictEqual(
        c.to_dict(),
        {'columnItems': [{'horizontalAlignment': 'START',
                          'widgets': [{'decoratedText': {'text': 'You are using '
                                                         "Bonetti's defense "
                                                         'against me!'}},
                                      {'decoratedText': {'text': 'You must expect me '
                                                         'to respond with '
                                                         'Capaferro.'}}]},
                         {'horizontalAlignment': 'END',
                          'widgets': [{'decoratedText': {'text': 'I thought it fitting '
                                                         'considering the '
                                                         'rocky terrain.'}},
                                      {'decoratedText': {'text': 'Natually, but I find '
                                                         'Tybalt cancels out '
                                                         "Capaferro, don't "
                                                         'you?'}}]}]}

    )

  def test_two_columns_multiple_widgets_misaligned(self) -> None:
    c1 = Column(horizontal_alignment=Column.HorizontalAlignment.START,
                vertical_alignment=Column.VerticalAlignment.TOP,
                widgets=[
                    DecoratedText(
                        text="You are using Bonetti's defense against me!"),
                    DecoratedText(
                        text="You must expect me to respond with Capaferro."),
                    DecoratedText(
                        text="Only if your enemy hasn't studied his Agrippa. Which I have!"),
                ])
    c2 = Column(horizontal_alignment=Column.HorizontalAlignment.END,
                vertical_alignment=Column.VerticalAlignment.TOP,
                widgets=[
                    DecoratedText(
                        text="I thought it fitting considering the rocky terrain."),
                    DecoratedText(
                        text="Natually, but I find Tybalt cancels out Capaferro, don't you?"),
                ])
    c = Columns(column_items=[c1, c2,])

    self.assertDictEqual(
        c.to_dict(),
        {'columnItems': [{'horizontalAlignment': 'START',
                          'verticalAlignment': 'TOP',
                          'widgets': [{'decoratedText': {'text': 'You are using '
                                                         "Bonetti's defense "
                                                         'against me!'}},
                                      {'decoratedText': {'text': 'You must expect me '
                                                         'to respond with '
                                                         'Capaferro.'}},
                                      {'decoratedText': {'text': 'Only if your enemy '
                                                         "hasn't studied his "
                                                         'Agrippa. Which I '
                                                         'have!'}}]},
                         {'horizontalAlignment': 'END',
                          'verticalAlignment': 'TOP',
                          'widgets': [{'decoratedText': {'text': 'I thought it fitting '
                                                         'considering the '
                                                         'rocky terrain.'}},
                                      {'decoratedText': {'text': 'Natually, but I find '
                                                         'Tybalt cancels out '
                                                         "Capaferro, don't "
                                                         'you?'}}]}]}

    )
