# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import types

import pytest

from pyliff.note import Notes


@pytest.mark.test
def test_pyliff_unit(file_units_xliff):
    f1 = file_units_xliff.files.next()
    units = f1.units
    u1 = units.next()

    assert u1.id == "u1"
    assert u1.name == "unit 1"
    assert u1.can_resegment is False
    assert u1.translate is True
    assert u1.src_dir == "ltr"
    assert u1.trg_dir == "rtl"
    assert u1.unit_type == "th:test_unit_1"

    u2 = units.next()
    assert u2.id == "u2"
    assert u2.name == "unit 2"
    assert u2.can_resegment is True
    assert u2.translate is False
    assert u2.src_dir == "rtl"
    assert u2.trg_dir == "ltr"
    assert u2.unit_type == "th:test_unit_2"

    u3 = units.next()
    assert u3.id == "u3"
    assert u3.name == ""
    assert u3.can_resegment is None
    assert u3.translate is None
    assert u3.src_dir == "auto"
    assert u3.trg_dir == "auto"
    assert u3.unit_type is None


@pytest.mark.test
def test_pyliff_unit_notes(file_units_xliff):
    f1 = file_units_xliff.files.next()
    units = f1.units
    u1 = units.next()

    # notes is a Note instance
    assert isinstance(u1.notes, Notes)


@pytest.mark.test
def test_pyliff_unit_segments(file_units_xliff):
    f1 = file_units_xliff.files.next()
    units = f1.units
    u1 = units.next()

    # segments is a generator
    assert isinstance(u1.segments, types.GeneratorType)

    # which is refreshed every time you ask for it
    assert len([x for x in u1.segments]) == 3
    assert len([x for x in u1.segments]) == 3
