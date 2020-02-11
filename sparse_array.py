import pytest

class SparseArray:
    def __init__(self, arr, size):
        self.size = size
        self.map = {}

        orig_arr_size = len(arr)
        for i, e in enumerate(arr):
            if i >= orig_arr_size:
                break
            if e != 0:
                map[i] = e

    def check_bounds(self, i):
        if i < 0 or i >= self.size:
            raise IndexError()
    
    def set(self, i, v):
        self.check_bounds(i)
        self.map[i] = v

    def get(self, i):
        self.check_bounds(i)
        v = self.map.get(i)
        if v is None:
            return 0
        return v

    def display(self):
        print("map : {}, size: {}".format(self.map, self.size))


def test_p134_1():
    arr = SparseArray([0, 0, 0], 5)
    arr.display()
    assert arr.get(0) == 0
    arr.display()
    assert arr.get(3) == 0

    with pytest.raises(IndexError):
        assert arr.get(-1)
        assert arr.get(-1, 0)
        assert arr.get(5)
        assert arr.set(5, 0)

    arr.set(0, 1)
    arr.display()
    assert arr.get(0) == 1

    arr.set(4, 1)
    arr.display()
    assert arr.get(4) == 1

if __name__ == "__main__":
    test_p134_1()