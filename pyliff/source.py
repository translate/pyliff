# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from .base import XMLObject


class Source(XMLObject):

    @property
    def text(self):
        # this should probably be a list of elements rather than `text`
        return self.xml.text or ""
