import heapq
from typing import List

import pytest


class KthLargest:
    """
    Increasing Array
    """

    def __init__(self, k: int, nums: List[int]):
        self.data = [float("-inf")] * k
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        for i, n in enumerate(self.data):
            if val >= n:
                for j in range(len(self.data) - 1, i, -1):
                    self.data[j] = self.data[j - 1]
                self.data[i] = val
                break
        return self.data[-1]


class KthLargest2:
    """
    Heap
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


solutions = [
    KthLargest,
    KthLargest2,
]


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    ops = ["KthLargest", "add", "add", "add", "add", "add"]
    args = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    expected_outputs = [None, 4, 5, 5, 8, 8]
    obj = solution(*args[0])
    actual_outputs = [None]
    for op, arg in zip(ops[1:], args[1:]):
        actual_outputs.append(getattr(obj, op)(*arg))
    assert actual_outputs == expected_outputs
