PyLIFF
=======

PyLIFF provides a pythonic representation of XLIFF 2.0 files.

Currently XLIFF data can only be read. In future versions you
will be able to manipulate the XLIFF data and serialize it back
to a file. 

The PyLIFF class is instantiated with a unicode string, and is
parsed using a DOM XML parser.

This means its not currently very efficient for handling very
large files or streams.


Installation
------------

Installation can be done via pip for the github repository::

   pip install -e git+https://github.com/translate/pyliff


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




