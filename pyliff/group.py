# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from .base import LIFFObject
from .unit import Unit


class Group(LIFFObject):

    @property
    def units(self):
        return (Unit(self.li, x) for x in self.xpath("xliff:unit"))

    @property
    def groups(self):
        return (Group(self.li, x) for x in self.xpath("xliff:group"))
