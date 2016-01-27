# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import pytest

from pyliff.source import Source
from pyliff.target import Target


@pytest.mark.test
def test_pyliff_unit_segment(file_units_xliff):
    f1 = file_units_xliff.files.next()
    units = f1.units
    segments = units.next().segments

    s1 = segments.next()
    assert s1.id == "s1"
    assert s1.can_resegment is True
    assert s1.state == "translated"
    assert s1.sub_state == "th:sub-translated"
    assert isinstance(s1.source, Source)
    assert isinstance(s1.target, Target)

    s2 = segments.next()
    assert s2.id == "s2"
    assert s2.can_resegment is False
    assert s2.state == "reviewed"
    assert s2.sub_state == "th:sub-reviewed"
    assert isinstance(s2.source, Source)
    assert isinstance(s2.target, Target)

    s3 = segments.next()
    assert s3.id is None
    assert s3.can_resegment is None
    assert s3.state == "initial"
    assert s3.sub_state is None
    assert isinstance(s3.source, Source)
    assert s3.target is None
