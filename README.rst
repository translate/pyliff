PyLIFF
=======

PyLIFF provides a pythonic representation of XLIFF 2.0 files.


.. image:: https://img.shields.io/travis/translate/pyliff.svg?style=flat-square
    :alt: Build Status
    :target: https://travis-ci.org/translate/pyliff

.. image:: https://coveralls.io/repos/translate/pyliff/badge.png?branch=master
    :alt: Coverage Status
    :target: https://coveralls.io/r/translate/pyliff?branch=master



Installation
------------

Installation can be done via pip for the github repository::

   pip install -e git+https://github.com/translate/pyliff


Development
-----------

If you wish to contribute or have any questions regarding usage
please checkout:


.. image:: https://img.shields.io/gitter/room/translate/dev.svg?style=flat-square
   :alt: Join the chat at https://gitter.im/translate/dev
   :target: https://gitter.im/translate/dev


Status
------

Pre-alpha - most of the core XLIFF 2.0 schema is modelled,
although there are still significant gaps.

Currently XLIFF data can only be read. In future versions you
will be able to manipulate the XLIFF data and serialize it back
to a file. 

The PyLIFF class is instantiated with a unicode string, and is
parsed using a DOM XML parser.

This means its not currently very efficient for handling very
large files or streams.


Usage
-----

.. code-block:: python

   from pyliff import PyLIFF

   XLIFF_EXAMPLE = u"""
   <?xml version="1.0" encoding="utf-8"?>
   <xliff xmlns="urn:oasis:names:tc:xliff:document:2.0"
          version="2.0"
	  srcLang="en"
	  trgLang="es">
   </xliff>
   """

   liff = PyLIFF(XLIFF_EXAMPLE)




