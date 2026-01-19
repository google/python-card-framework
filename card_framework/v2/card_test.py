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

from .card import Card, CardWithId
from .card_header import CardHeader
from .section import Section
from .widgets.text_paragraph import TextParagraph
from .widgets.date_time_picker import DateTimePicker


class CardTest(unittest.TestCase):
  def test_simple_render(self) -> None:
    self.maxDiff = None
    header = CardHeader(title='Princess Bride')
    section = Section()
    section.add_widget(TextParagraph(text="Inconceivable!"))
    card = Card()
    card.header = header
    card.add_section(section)
    output = card.render()

    self.assertDictEqual(
        output,
        {
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
    card.add_section(section)
    output = card.render()

    self.assertDictEqual(
        output,
        {
            'card': {
                'sections': [{
                    'widgets': [
                        {'textParagraph': {
                            'text': 'Inconceivable!'
                        }}]}]}})

  def test_tag_override(self) -> None:
    self.maxDiff = None
    section = Section()
    section.add_widget(TextParagraph(text="Inconceivable!"))
    card = Card()
    card.add_section(section)
    card.__TAG_OVERRIDE__ = 'pushCard'
    output = card.render()

    self.assertDictEqual(
        output,
        {
            'pushCard': {
                'sections': [{
                    'widgets': [
                        {'textParagraph': {
                            'text': 'Inconceivable!'
                        }}]}]}})


class CardWithIdTest(unittest.TestCase):
  def test_simple_render(self) -> None:
    self.maxDiff = None
    header = CardHeader(title='Princess Bride')
    section = Section()
    section.add_widget(TextParagraph(text="Inconceivable!"))
    card = CardWithId()
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

  def test_simple_render_sub_card(self) -> None:
    self.maxDiff = None
    header = CardHeader(title='Princess Bride')
    section = Section()
    section.add_widget(TextParagraph(text="Inconceivable!"))
    card = CardWithId()
    card.card_id = 'vizzini'
    card.header = header
    card.add_section(section)
    output = card.card().render()
    print(output)

    self.assertDictEqual(
        output,
        {
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
    card = CardWithId()
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
    card = CardWithId()
    card.add_section(section)
    output = card.render()

    self.assertTrue('cardId' in output)
    self.assertIsNotNone(output['cardId'])

  def test_tag_override(self) -> None:
    self.maxDiff = None
    header = CardHeader(title='Princess Bride')
    section = Section()
    section.add_widget(TextParagraph(text="Inconceivable!"))
    card = CardWithId()
    card.__TAG_OVERRIDE__ = 'pushCard'
    card.card_id = 'vizzini'
    card.header = header
    card.add_section(section)
    output = card.render()

    self.assertDictEqual(
        output,
        {
            'cardId': 'vizzini',
            'pushCard': {
                'header': {'title': 'Princess Bride'},
                'sections': [{
                    'widgets': [
                        {'textParagraph': {
                            'text': 'Inconceivable!'
                        }}]}]}})

  def test_tag_override_nested_card(self) -> None:
    self.maxDiff = None
    header = CardHeader(title='Princess Bride')
    header = CardHeader(title='Princess Bride')
    section = Section()
    section.add_widget(TextParagraph(text="Inconceivable!"))
    card_with_id = CardWithId()
    card_with_id.card_id = 'vizzini'
    card_with_id.header = header
    card_with_id.add_section(section)

    card = card_with_id.card()
    card.__TAG_OVERRIDE__ = 'pushCard'
    output = card.render()

    self.assertDictEqual(
        output,
        {
            'pushCard': {
                'header': {'title': 'Princess Bride'},
                'sections': [{
                    'widgets': [
                        {'textParagraph': {
                            'text': 'Inconceivable!'
                        }}]}]}})
