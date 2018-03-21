# encoding: utf-8


"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

import itertools
from collections import OrderedDict

import pytest
from typepy import StrictLevel, Typecode
from typepy.type import Dictionary


nan = float("nan")
inf = float("inf")


class Test_Dictionary_is_type(object):

    @pytest.mark.parametrize(
        ["value", "strict_level", "expected"],
        [
            [[["a", 1]], StrictLevel.MIN, True],
            [[["a", 1]], StrictLevel.MAX, False],
            [(("a", 1), ), StrictLevel.MIN, True],
            [(("a", 1), ), StrictLevel.MAX, False],
        ] + list(itertools.product(
            [{}, {"a": 1, "b": 2}, OrderedDict(a=1, b=1)],
            [StrictLevel.MIN, StrictLevel.MAX],
            [True],
        )) + list(itertools.product(
            [1, "a", nan, True, None],
            [StrictLevel.MIN, StrictLevel.MAX],
            [False],
        )))
    def test_normal(self, value, strict_level, expected):
        type_object = Dictionary(value, strict_level)

        assert type_object.is_type() == expected
        assert type_object.typecode == Typecode.DICTIONARY
