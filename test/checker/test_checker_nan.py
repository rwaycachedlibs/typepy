# encoding: utf-8


"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

import itertools
from decimal import Decimal

import pytest
import six
from typepy import StrictLevel, Typecode
from typepy.type import Nan


nan = float("nan")
inf = float("inf")


class Test_Nan_is_type(object):

    @pytest.mark.parametrize(
        ["value", "strict_level", "expected"],
        list(itertools.product(
            [0.0, six.MAXSIZE, "0", inf, None],
            [StrictLevel.MIN, StrictLevel.MAX],
            [False]
        )) + list(itertools.product(
            [nan, Decimal("NaN")],
            [StrictLevel.MIN, StrictLevel.MAX],
            [True]
        )) + [
            ["nan", StrictLevel.MIN, True],
            ["nan", StrictLevel.MAX, False],
            ["-Nan", StrictLevel.MIN, True],
            ["-Nan", StrictLevel.MAX, False],
            ["NAN", StrictLevel.MIN, True],
            ["NAN", StrictLevel.MAX, False],
        ])
    def test_normal(self, value, strict_level, expected):
        type_checker = Nan(value, strict_level)

        assert type_checker.is_type() == expected
        assert type_checker.typecode == Typecode.NAN
