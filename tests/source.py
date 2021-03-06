# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import pytest


@pytest.mark.test
def test_pyliff_source(file_units_xliff):
    f1 = file_units_xliff.files.next()
    units = f1.units
    segments = units.next().segments

    s1 = segments.next()
    assert s1.source.text == 'Unit 1'

    s2 = segments.next()
    assert s2.source.text == 'Unit 1 - part 2'

    s3 = segments.next()
    assert s3.source.text == 'Unit 1 - part 3'
