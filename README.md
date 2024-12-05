# Python Card Framework

This is a library designed to allow Python developers to treat the Chat API
JSON to be generated for cards and dialogs as objects, each capable of
rendering themselves into valid JSON instead of hand-crafting or cut-and-pasting
JSON in large blocks.

The exact JSON that is being rendered can be found in the official Google
Developer Docs pages here: https://developers.google.com/chat/api/reference/rest/v1/spaces.messages?hl=en

## Intention

In order to generate or send messages from a chat application to the user, the
messages must be formed of valid JSON objects. In the event that the message is
malformed, a simple 'Chat App not responding' message is returned. This leads
to the developer having to insert large blocks of JSON in their Python code,
much of which is boiler-plate and can easily lead to hard to find cut and paste
errors.

As a result this library of objects has been created to alleviate the problem.
The developer can now create and manipulate first-class Python objects which
know how to correctly render themselves. Thus, instead of inserting this:

```python
  return {
    "sections": [
        {
          "widgets": [
            {
              "decoratedText": {
                "topLabel": "Hello, my name is Inigo Montoya",
                "text": "You killed my father. Prepare to die.",
                "startIcon": {
                  "knownIcon": "PERSON"
                }
              }
            }
        ]
      }
    ],
    "header": {
      "title": "The Princess Bride",
      "imageUrl": "https://source.unsplash.com/featured/320x180?nature&sig=8",
      "imageType": "CIRCLE"
    }
  }
```

... the developer can instead do this (with the appropriate `import`s, of course):
```python
from card_framework.v2 import Card, CardHeader, Message, Section
from card_framework.v2.widgets import DecoratedText, Icon
```

```python
text = DecoratedText(top_label='Hello, my name is Inigo Montoya',
                     text='You killed my father. Prepare to die.',
                     start_icon=Icon(known_icon=Icon.KnownIcon.PERSON))
widgets = [text]
header = CardHeader(title='The Princess Bride',
                    image_url='https://source.unsplash.com/featured320x180?nature&sig=8')
card = Card(header=header, sections=[Section(widgets=widgets)])

return Message(cards=[card]).render()
```

which will return the correct JSON.
