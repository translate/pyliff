# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import pytest

from pyliff import PyLIFF

ROOT_XLIFF = u"""
<?xml version="1.0" encoding="utf-8"?>
<xliff xmlns="urn:oasis:names:tc:xliff:document:2.0"
       version="2.0" srcLang="en" trgLang="es">
</xliff>
"""


@pytest.fixture
def root_xliff():
    return PyLIFF(ROOT_XLIFF.strip())


@pytest.mark.test
def test_pyliff_xliff(root_xliff):
    assert root_xliff.version == 2.0
    assert root_xliff.src_lang == "en"
    assert root_xliff.trg_lang == "es"
