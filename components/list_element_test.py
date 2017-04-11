# -*- coding: utf-8 -*-
from meya import Component
from meya.cards import (
    Image, ImageWithButtons, Card, Cards, TextWithButtons,
    Receipt, Location, Video, Audio, File, List, Element)


class ListElementTest(Component):
    def start(self):
        text = "Hello, world!"
        print List, Element
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")
