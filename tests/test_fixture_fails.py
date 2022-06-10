# -*- coding: utf-8 -*-
# should return 1

import pytest

@pytest.fixture
def fixture_that_fails():
    raise RuntimeError
    pass

def test_should_ok(fixture_that_fails):
    assert 1
