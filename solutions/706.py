import pytest


class MyHashMap:
    """
    One big array
    """

    size = 10**6 + 1

    def __init__(self):
        self.data = [-1] * self.size

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = -1


class MyHashMap2:
    """
    Use nested array
    """

    size = 1000

    def __init__(self):
        self.data = [[] for _ in range(self.size)]

    def hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        for i, (k, _) in enumerate(self.data[index]):
            if k == key:
                self.data[index][i][-1] = value
                break
        else:
            self.data[index].append([key, value])

    def get(self, key: int) -> int:
        index = self.hash(key)
        for k, v in self.data[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        for i, (k, _) in enumerate(self.data[index]):
            if k == key:
                self.data[index].pop(i)
                break


HashMaps = [
    MyHashMap,
    MyHashMap2,
]


@pytest.mark.parametrize("hmap", HashMaps)
def test_1(hmap):
    ops = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
    args = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
    expected_outputs = [None, None, None, 1, -1, None, 1, None, -1]
    obj = hmap()
    actual_outputs = [None]
    for op, arg in zip(ops[1:], args[1:]):
        actual_outputs.append(getattr(obj, op)(*arg))
    assert actual_outputs == expected_outputs


@pytest.mark.parametrize("hmap", HashMaps)
def test_2(hmap):
    ops = ["MyHashMap", "remove", "put", "put", "put", "put", "put", "put", "get", "put", "put"]
    args = [[], [2], [3, 11], [4, 13], [15, 6], [6, 15], [8, 8], [11, 0], [11], [1, 10], [12, 14]]
    obj = hmap()
    actual_outputs = [None]
    expected_outputs = [None, None, None, None, None, None, None, None, 0, None, None]
    for op, arg in zip(ops[1:], args[1:]):
        actual_outputs.append(getattr(obj, op)(*arg))
    assert actual_outputs == expected_outputs
