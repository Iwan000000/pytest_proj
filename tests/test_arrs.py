import pytest

from utils import arrs

@pytest.fixture
def arrey():
    return [1,2,3,4,5]



def test_get(arrey):
    assert arrs.get(arrey, 2, "test") == 3
    assert arrs.get(arrey, 10, "test") == "test"





def test_slice(arrey):
    assert arrs.my_slice(arrey, 1, 3) == [2, 3]
    assert arrs.my_slice(arrey, 1) == [2, 3, 4, 5]
    assert arrs.my_slice([],1,4) == []
    assert arrs.my_slice(arrey, -4, -1) == [2, 3, 4]
    assert arrs.my_slice(arrey, start=-2) == [4, 5]
    assert arrs.my_slice(arrey, end=-2) == [1, 2, 3]
