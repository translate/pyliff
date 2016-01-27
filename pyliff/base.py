# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from lxml import etree

from .decorators import attribute


XLIFF_NS = 'urn:oasis:names:tc:xliff:document:2.0'


class XMLObject(object):

    def __init__(self, li, xml):
        self.li = li
        self.xml = xml

    def xpath(self, path):
        return self.xml.xpath(
            path,
            namespaces={'xliff': XLIFF_NS})

    def serialize(self):
        return etree.tostring(self.xml)


class LIFFObject(XMLObject):

    @property
    def id(self):
        return self.xml.attrib["id"]

    @attribute(
        "canResegment",
        choices=["yes", "no"],
        default=None)
    def can_resegment(self, value):
        if value is None:
            return
        return value == "yes" and True or False

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

    @attribute(
        choices=["yes", "no"],
        default=None)
    def translate(self, value):
        if value is None:
            return
        return value == "yes" and True or False
