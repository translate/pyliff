# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import os

from lxml import etree

from .decorators import attribute, children
from .file import File


XLIFF_NS = 'urn:oasis:names:tc:xliff:document:2.0'


class LanguageInterchangeFormat(object):

    attr_prefix = "/@"
    node_prefix = "/xliff:"

    def __init__(self, src):
        # todo validate src
        self.src = src
        self.original_src = src

    @property
    def base_xml(self):
        return etree.fromstring(
            self.src.encode(),
            parser=etree.XMLParser(
                ns_clean=True,
                recover=True,
                encoding='utf-8'))

    @children("file")
    def files(self, values):
        return (
            File(self, f)
            for f
            in values)

    @property
    def root_path(self):
        return "/xliff:xliff"

    def serialize(self, format=None):
        return etree.tostring(self.xml)

    @attribute("srcLang", required=True)
    def src_lang(self, value):
        return value

    @attribute("trgLang", default="")
    def trg_lang(self, value):
        return value

    @attribute
    def version(self, value):
        return float(value)

    @property
    def xslt(self):
        if self.xslt_template:
            return etree.XSLT(self.xslt_template)
        return None

    def xpath(self, path):
        return self.xml.xpath(
            self.root_path + path,
            namespaces={'xliff': XLIFF_NS})

    @property
    def xslt_template(self):
        if not getattr(self, "__xslt__", None):
            return None
        xslt_path = os.path.join(
            os.path.dirname(__file__),
            "xslt",
            self.__xslt__)
        with open(xslt_path) as f:
            xslt = f.read()
        return etree.XML(xslt)

    @property
    def xml(self):
        if self.xslt:
            return self.xslt(self.base_xml)
        return self.base_xml
