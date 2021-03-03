import pytest
from app import soma


@pytest.mark.parametrize('a,b,expected', [(1, 1, 2), (-1, 1, 0), (-1, -1, -2), (1.1, 1.1,2.2), (-1.2, -1.2,-2.4)])
def test_soma(a,b, expected):
    assert soma(a,b) == expected
