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


from card_framework.v2.annotation import Annotation, SlashCommandMetadata, UserMentionMetadata
from card_framework.v2.user import User


class AnnotationTest(unittest.TestCase):
  def test_render_slash_command(self) -> None:
    a = Annotation(type=Annotation.AnnotationType.SLASH_COMMAND)
    s = SlashCommandMetadata()
    s.type = SlashCommandMetadata.SlashCommandMetadataType.INVOKE
    s.command_id = 1
    s.command_name = '/tothepain'
    a.slash_command = s

    self.assertDictEqual(
        a.render(),
        {'annotation': {'slashCommand': {'commandId': 1,
                                         'commandName': '/tothepain',
                                         'type': 'INVOKE'},
                        'type': 'SLASH_COMMAND'}}
    )

  def test_render_user_mention(self) -> None:
    a = Annotation(Annotation.AnnotationType.USER_MENTION)
    u = UserMentionMetadata()
    u.type = UserMentionMetadata.UserMentionMetadataType.MENTION
    user = User()
    user.type = User.UserType.HUMAN
    user.name = 'westley'
    user.display_name = 'Dread Pirate Roberts'
    u.user = user
    a.user_mention = u

    self.assertDictEqual(
        a.render(),
        {'annotation': {
            'type': 'USER_MENTION',
            'userMention': {
                'type': 'MENTION',
                'user': {
                    'displayName': 'Dread Pirate Roberts',
                    'name': 'westley',
                    'type': 'HUMAN'
                }
            }
        }
        })
