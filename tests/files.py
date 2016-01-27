# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import pytest

import types


from pyliff.file import File
from pyliff.note import Notes


@pytest.mark.test
def test_pyliff_files(files_xliff):

    # files_xliff.files is a generator
    assert isinstance(files_xliff.files, types.GeneratorType)

    # which is refreshed every time you ask for it
    assert len([x for x in files_xliff.files]) == 3
    assert len([x for x in files_xliff.files]) == 3


@pytest.mark.test
def test_pyliff_file(files_xliff):
    files = files_xliff.files

    f1 = files.next()
    assert isinstance(f1, File)
    assert f1.id == "f1"
    assert f1.can_resegment is True
    assert f1.original == "/foo/bar"
    assert f1.src_dir == "ltr"
    assert f1.trg_dir == "rtl"

    f2 = files.next()
    assert isinstance(f2, File)
    assert f2.id == "f2"
    assert f2.can_resegment is False
    assert f2.original == "http://foo/bar"
    assert f2.src_dir == "rtl"
    assert f2.trg_dir == "ltr"

    f3 = files.next()
    assert isinstance(f3, File)
    assert f3.id == "f3"
    assert f3.can_resegment is True
    assert f3.original is None
    assert f3.src_dir == "auto"
    assert f3.trg_dir == "auto"


@pytest.mark.test
def test_pyliff_file_units(file_units_xliff):
    files = file_units_xliff.files
    f1 = files.next()

    # units is a generator
    assert isinstance(f1.units, types.GeneratorType)

    # which is refreshed every time you ask for it
    assert len([x for x in f1.units]) == 3
    assert len([x for x in f1.units]) == 3


@pytest.mark.test
def test_pyliff_file_groups(file_groups_xliff):
    files = file_groups_xliff.files
    f1 = files.next()

    # units is a generator
    assert isinstance(f1.groups, types.GeneratorType)

    # which is refreshed every time you ask for it
    assert len([x for x in f1.groups]) == 3
    assert len([x for x in f1.groups]) == 3


@pytest.mark.test
def test_pyliff_file_notes(file_notes_xliff):
    files = file_notes_xliff.files
    f1 = files.next()

    # notes is a Note instance
    assert isinstance(f1.notes, Notes)
