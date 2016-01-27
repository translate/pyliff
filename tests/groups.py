# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import types

import pytest


@pytest.mark.test
def test_pyliff_group(file_groups_xliff):
    f1 = file_groups_xliff.files.next()
    groups = f1.groups
    g1 = groups.next()

    assert g1.id == "g1"


@pytest.mark.test
def test_pyliff_group_units(file_groups_xliff):
    files = file_groups_xliff.files
    f1 = files.next()

    groups = f1.groups
    g1 = groups.next()

    # units is a generator
    assert isinstance(g1.units, types.GeneratorType)

    # which is refreshed every time you ask for it
    assert len([x for x in g1.units]) == 3
    assert len([x for x in g1.units]) == 3


@pytest.mark.test
def test_pyliff_group_groups(file_groups_xliff):
    files = file_groups_xliff.files
    f1 = files.next()

    groups = f1.groups
    g1 = groups.next()

    # groups is a generator
    assert isinstance(g1.groups, types.GeneratorType)

    # which is refreshed every time you ask for it
    assert len([x for x in g1.groups]) == 3
    assert len([x for x in g1.groups]) == 3
