# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from .base import LIFFObject
from .note import Note
from .segment import Segment


class Unit(LIFFObject):

    @property
    def unit_type(self):
        return self.xml.attrib["type"]

    @property
    def notes(self):
        return (Note(self.li, x) for x in self.xpath("xliff:notes/xliff:note"))

    @property
    def segments(self):
        return [Segment(self.li, x) for x in self.xpath("xliff:segment")]
