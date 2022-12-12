from collections import deque

import pytest


class MyStack:
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        return len(self.data) == 0


class MyStack2:
    def __init__(self):
        self.s = deque()

    def push(self, x: int) -> None:
        self.s.appendleft(x)

    def pop(self) -> int:
        return self.s.popleft()

    def top(self) -> int:
        return self.s[0]

    def empty(self) -> bool:
        return len(self.s) == 0


solutions = [
    MyStack,
    MyStack2,
]


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    steps = ["MyStack", "push", "push", "top", "pop", "empty"]
    args = [[], [1], [2], [], [], []]
    actual = []
    expected = [None, None, None, 2, 2, False]
    obj = solution()
    for s, arg in zip(steps[1:], args[1:]):
        func = getattr(obj, s)
        actual.append(func(*arg))
    assert actual == expected[1:]
