# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from .base import LIFFObject
from .decorators import children
from .unit import Unit


class Group(LIFFObject):

    @children("unit")
    def units(self, values):
        return (
            Unit(self.li, x)
            for x
            in values)

    @children("group")
    def groups(self, values):
        return (
            Group(self.li, x)
            for x
            in values)
