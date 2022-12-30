from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Reverse Scan
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def replaceElements(self, arr: List[int]) -> List[int]:
        prev_max = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], prev_max = prev_max, max(arr[i], prev_max)
        return arr


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "replaceElements",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(arr=[17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(arr=[400]) == [-1]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(arr=[900, 1]) == [1, -1]
