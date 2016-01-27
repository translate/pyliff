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
def test_pyliff_notes(file_notes_xliff):
    f1 = file_notes_xliff.files.next()

    # file.notes is a Notes object
    assert isinstance(f1.notes, Notes)

    # Notes.notes is a generator
    assert isinstance(f1.notes.notes, types.GeneratorType)

    # you can iterate the Notes object directly
    # its refreshed every time you ask for it
    assert len([x for x in f1.notes]) == 3
    assert len([x for x in f1.notes]) == 3


@pytest.mark.test
def test_pyliff_notes_note(file_notes_xliff):
    f1 = file_notes_xliff.files.next()
    notes = f1.notes.notes

    n1 = notes.next()
    assert n1.id == "n1"
    assert n1.category == "c1"
    assert n1.applies_to == "u1"
    assert n1.priority == 3
    assert n1.text == "Note 1"

    n2 = notes.next()
    assert n2.id == "n2"
    assert n2.category == "c2"
    assert n2.applies_to == "u2"
    assert n2.priority is None
    assert n2.text == "Note 2"

    n3 = notes.next()
    assert n3.id is None
    assert n3.category is None
    assert n3.applies_to is None
    assert n3.priority is None
    assert n3.text == ""
