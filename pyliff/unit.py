# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from .base import LIFFObject
from .decorators import attribute, children, node
from .note import Notes
from .segment import Segment


class Unit(LIFFObject):

    @attribute(default="")
    def name(self, value):
        return value

    @attribute("type")
    def unit_type(self, value):
        return value

    @node
    def notes(self, value):
        return Notes(self.li, value)

    @children("segment")
    def segments(self, values):
        return (
            Segment(self.li, x)
            for x
            in values)
