# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from lxml import etree


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

    @property
    def can_resegment(self):
        return self.xml.attrib["canResegment"]

    @property
    def src_dir(self):
        return self.xml.attrib["srcDir"]

    @property
    def translate(self):
        return self.xml.attrib["translate"]

    @property
    def target_dir(self):
        return self.xml.attrib["targetDir"]
