#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the pyspark_mllib module.
"""
import pytest

from pyspark_mllib import pyspark_mllib


def test_something():
    assert True


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise(ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_pyspark_mllib(an_object):
    assert an_object == {}
