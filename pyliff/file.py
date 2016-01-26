# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from .base import XMLObject
from .decorators import attribute, children
from .note import Notes
from .unit import Unit
from .group import Group


class File(XMLObject):

    @attribute(required=True)
    def id(self, value):
        return value

    @attribute(
        "canResegment",
        choices=["yes", "no"],
        default="yes")
    def can_resegment(self, value):
        return value == "yes" and True or False

    @attribute
    def original(self, value):
        return value

    @attribute(
        "srcDir",
        choices=["ltr", "rtl", "auto"],
        default="auto")
    def src_dir(self, value):
        return value

    @attribute(
        "trgDir",
        choices=["ltr", "rtl", "auto"],
        default="auto")
    def trg_dir(self, value):
        return value

    @property
    def notes(self):
        return Notes(self.li, self.xpath("xliff:notes"))

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
