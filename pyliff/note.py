# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from .base import XMLObject

from .decorators import children


class Notes(XMLObject):

    @children("note")
    def notes(self, values):
        return (
            Note(self.li, x)
            for x
            in values)


class Note(XMLObject):

    @property
    def id(self):
        return self.xml.attrib["id"]

    @property
    def applies_to(self):
        return self.xml.attrib.get("applies_to", None)

    @property
    def category(self):
        return self.xml.attrib.get("category", None)

    @property
    def priority(self):
        return self.xml.attrib.get("priority", None)

    @property
    def text(self):
        return self.xml.text
