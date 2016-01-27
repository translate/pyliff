# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import pytest

from pyliff import PyLIFF


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
    <unit id="u1"
          name="unit 1"
          canResegment="no"
          translate="yes"
          srcDir="ltr"
          trgDir="rtl"
          type="th:test_unit_1">
      <notes>
        <note id="n1"
              appliesTo="u1"
              category="c1"
              priority="3">Note 1</note>
        <note id="n2"
              appliesTo="u2"
              category="c2">Note 2</note>
        <note></note>
      </notes>
      <segment id="s1"
               canResegment="yes"
               state="translated"
               subState="th:sub-translated">
        <source>Unit 1</source>
        <target>Unit 1 target</target>
      </segment>
      <segment id="s2"
               canResegment="no"
               state="reviewed"
               subState="th:sub-reviewed">
        <source>Unit 1 - part 2</source>
        <target>Unit 1 target - part 2</target>
      </segment>
      <segment>
        <source>Unit 1 - part 3</source>
      </segment>
    </unit>
    <unit id="u2"
          name="unit 2"
          canResegment="yes"
          translate="no"
          srcDir="rtl"
          trgDir="ltr"
          type="th:test_unit_2">
      <segment>
        <source>Unit 2</source>
      </segment>
    </unit>
    <unit id="u3">
      <segment>
        <source>Unit 3</source>
      </segment>
    </unit>
  </file>
</xliff>
"""

FILE_NOTES_XLIFF = u"""
<?xml version="1.0" encoding="utf-8"?>
<xliff xmlns="urn:oasis:names:tc:xliff:document:2.0"
       version="2.0" srcLang="en">
  <file id="f1">
    <notes>
      <note id="n1"
            appliesTo="u1"
            category="c1"
            priority="3">Note 1</note>
      <note id="n2"
            appliesTo="u2"
            category="c2">Note 2</note>
      <note></note>
    </notes>
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


@pytest.fixture
def file_notes_xliff():
    return PyLIFF(FILE_NOTES_XLIFF.strip())
