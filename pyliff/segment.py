# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from .base import XMLObject
from .decorators import attribute, node
from .source import Source
from .target import Target


SEGMENT_STATES = [
    "initial",
    "translated",
    "reviewed",
    "final"]


class Segment(XMLObject):

    @attribute
    def id(self, value):
        return value

    @attribute(
        "canResegment",
        choices=["yes", "no"],
        default=None)
    def can_resegment(self, value):
        if value is None:
            return
        return value == "yes" and True or False

    @node
    def source(self, value):
        return Source(self.li, value)

    @attribute(
        choices=SEGMENT_STATES,
        default="initial")
    def state(self, value):
        return value

    @attribute("subState")
    def sub_state(self, value):
        return value

    @node
    def target(self, value):
        return Target(self.li, value)
