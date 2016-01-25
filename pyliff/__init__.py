# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.


from lxml import etree

from .liff import LanguageInterchangeFormat


class PyLIFF(LanguageInterchangeFormat):

    @property
    def xml(self):
        return etree.fromstring(
            self.src.encode(),
            parser=etree.XMLParser(
                ns_clean=True,
                recover=True,
                encoding='utf-8'))

    @property
    def namespaces(self):
        pass

    @property
    def root_path(self):
        return "/xliff:xliff"

    def serialize(self):
        return etree.tostring(self.xml)

    def xpath(self, path):
        return self.xml.xpath(
            self.root_path + path,
            namespaces={'xliff': 'urn:oasis:names:tc:xliff:document:2.0'})
