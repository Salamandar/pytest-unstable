# -*- coding: utf-8 -*-

import pytest

# @pytest.mark.xfail(strict=False)

@pytest.mark.unstable
def test_unstable():
    assert 0


def test_should_ok():
    assert 1
