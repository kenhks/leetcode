from collections import deque

import pytest


class MinStack:
    """
    A stack with two values
    """

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        new_min = min(val, self.getMin()) if len(self.stack) > 0 else val
        self.stack.append((val, new_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class MinStack2:
    """
    Two seperate stack
    """

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        if len(self.min_stack) > 0:
            new_min = min(self.getMin(), val)
        else:
            new_min = val
        self.stack.append(val)
        self.min_stack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


solutions = [
    MinStack,
    MinStack2,
]


@pytest.mark.parametrize("minstack", solutions)
def test_1(minstack):
    ops = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    args = [[], [-2], [0], [-3], [], [], [], []]
    expected_outputs = [None, None, None, None, -3, None, 0, -2]
    obj = minstack()
    actual_outputs = [None]
    for op, arg in zip(ops[1:], args[1:]):
        actual_outputs.append(getattr(obj, op)(*arg))
    assert actual_outputs == expected_outputs


@pytest.mark.parametrize("minstack", solutions)
def test_2(minstack):
    ops = ["MinStack", "push", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    args = [[], [-2], [-3], [0], [-3], [], [], [], []]
    expected_outputs = [None, None, None, None, None, -3, None, 0, -3]
    obj = minstack()
    actual_outputs = [None]
    for op, arg in zip(ops[1:], args[1:]):
        actual_outputs.append(getattr(obj, op)(*arg))
    assert actual_outputs == expected_outputs
