import pytest


class MyHashSet:
    """
    Big Array
    """

    size = 10**6 + 1

    def __init__(self):
        self.data = [False] * self.size

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]


class MyHashSet2:
    """
    Nested Array
    """

    size = 10000

    def __init__(self):
        self.data = [[]] * self.size

    def hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        if not self.contains(key):
            hash = self.hash(key)
            self.data[hash].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            hash = self.hash(key)
            self.data[hash].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.data[self.hash(key)]


solutions = [
    MyHashSet,
    MyHashSet2,
]


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    ops = ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
    args = [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    expected_outputs = [None, None, None, True, False, None, True, None, False]
    obj = solution(*args[0])
    actual_outputs = [None]
    for op, arg in zip(ops[1:], args[1:]):
        actual_outputs.append(getattr(obj, op)(*arg))
    assert actual_outputs == expected_outputs
