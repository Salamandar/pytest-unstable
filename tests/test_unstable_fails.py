# -*- coding: utf-8 -*-
# Should return 0

import pytest

@pytest.mark.unstable
def test_unstable():
    assert 0

def test_should_ok():
    assert 1
