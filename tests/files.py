# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import types

import pytest

from pyliff import PyLIFF
from pyliff.file import File


FILES_XLIFF = u"""
<?xml version="1.0" encoding="utf-8"?>
<xliff xmlns="urn:oasis:names:tc:xliff:document:2.0"
       version="2.0" srcLang="en">
  <file id="f1"
        canResegment="yes"
        original="/foo/bar"
        srcDir="ltr"
        trgDir="rtl">
    <unit id="u1" name="unit 1">
      <segment>
        <source>Unit 1</source>
      </segment>
    </unit>
  </file>
  <file id="f2"
        canResegment="no"
        original="http://foo/bar"
        srcDir="rtl"
        trgDir="ltr">
    <unit id="u2" name="unit 2">
      <segment>
        <source>Unit 2</source>
      </segment>
    </unit>
  </file>
  <file id="f3">
    <unit id="u3" name="unit 3">
      <segment>
        <source>Unit 3</source>
      </segment>
    </unit>
  </file>
</xliff>
"""

FILE_GROUPS_XLIFF = u"""
<?xml version="1.0" encoding="utf-8"?>
<xliff xmlns="urn:oasis:names:tc:xliff:document:2.0"
       version="2.0" srcLang="en">
  <file id="f1">
    <group id="g1"
           canResegment="yes"
           srcDir="ltr"
           trgDir="rtl">
      <unit id="u1" name="unit 1">
        <segment>
          <source>Unit 1</source>
        </segment>
      </unit>
      <unit id="u2" name="unit 2">
        <segment>
          <source>Unit 2</source>
        </segment>
      </unit>
      <unit id="u3" name="unit 3">
        <segment>
          <source>Unit 3</source>
        </segment>
      </unit>
    </group>
    <group id="g2">
      <unit id="u4" name="unit 4">
        <segment>
          <source>Unit 4</source>
        </segment>
      </unit>
    </group>
    <group id="g3">
      <unit id="u5" name="unit 5">
        <segment>
          <source>Unit 5</source>
        </segment>
      </unit>
    </group>
  </file>
</xliff>
"""


FILE_UNITS_XLIFF = u"""
<?xml version="1.0" encoding="utf-8"?>
<xliff xmlns="urn:oasis:names:tc:xliff:document:2.0"
       version="2.0" srcLang="en">
  <file id="f1"
        canResegment="yes"
        original="/foo/bar"
        srcDir="ltr"
        trgDir="rtl">
    <unit id="u1" name="unit 1">
      <segment>
        <source>Unit 1</source>
      </segment>
    </unit>
    <unit id="u2" name="unit 2">
      <segment>
        <source>Unit 2</source>
      </segment>
    </unit>
    <unit id="u3" name="unit 3">
      <segment>
        <source>Unit 3</source>
      </segment>
    </unit>
  </file>
</xliff>
"""


@pytest.fixture
def files_xliff():
    return PyLIFF(FILES_XLIFF.strip())


@pytest.fixture
def file_units_xliff():
    return PyLIFF(FILE_UNITS_XLIFF.strip())


@pytest.fixture
def file_groups_xliff():
    return PyLIFF(FILE_GROUPS_XLIFF.strip())


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
