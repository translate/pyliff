# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from .base import XMLObject
from .source import Source
from .target import Target


class Segment(XMLObject):

    @property
    def id(self):
        return self.xml.attrib["id"]

    @property
    def can_resegment(self):
        return self.xml.attrib.get("canResegment", None)

    @property
    def source(self):
        source = self.xpath("xliff:source")
        if source:
            return Source(self.li, source[0])
        else:
            # raise misconfiguration
            pass

    @property
    def state(self):
        return self.xml.attrib.get("state", None)

    @property
    def sub_state(self):
        return self.xml.attrib.get("sub_state", None)

    @property
    def target(self):
        target = self.xpath("xliff:target")
        if target:
            return Target(self.li, target[0])
