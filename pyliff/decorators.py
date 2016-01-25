# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import functools


def attribute(*args, **kwargs):
    if not args:
        return functools.partial(attribute, **kwargs)

    def wrapped(m):

        @functools.wraps(m)
        def method_wrapper(self):
            if args:
                attr = args[0]
            else:
                attr = m.func_name
            attr_prefix = getattr(self, "attr_prefix", "@")
            result = self.xpath("%s%s" % (attr_prefix, attr))
            if result:
                if kwargs.get("choices", None):
                    if result[0] in kwargs["choices"]:
                        return m(self, result[0])
                else:
                    return m(self, result[0])
            if "default" in kwargs:
                return m(self, kwargs["default"])

        return property(method_wrapper)

    if len(args) == 1 and callable(args[0]):
        method = args[0]
        args = []
        return wrapped(method)

    return wrapped


def children(*args, **kwargs):
    if not args:
        return functools.partial(children, **kwargs)

    def wrapped(m):

        @functools.wraps(m)
        def method_wrapper(self):
            if args:
                node = args[0]
            else:
                node = m.func_name
            node_prefix = getattr(self, "node_prefix", "xliff:")
            return m(self, self.xpath("%s%s" % (node_prefix, node)))

        return property(method_wrapper)

    if len(args) == 1 and callable(args[0]):
        method = args[0]
        args = []
        return wrapped(method)

    return wrapped
