# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from .base import XMLObject

from .decorators import attribute, children


class Notes(XMLObject):

    def __iter__(self):
        return self.notes

    @children("note")
    def notes(self, values):
        return (
            Note(self.li, x)
            for x
            in values)


class Note(XMLObject):

    @attribute
    def id(self, value):
        return value

    @attribute("appliesTo")
    def applies_to(self, value):
        return value

    @attribute
    def category(self, value):
        return value

    @attribute(
        choices=[str(i) for i in range(1, 11)])
    def priority(self, value):
        return int(value)

    @property
    def text(self):
        return self.xml.text or ""
