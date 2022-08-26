from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with hashmap
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for i in arr:
            if (i * 2) in seen or (i / 2) in seen:
                return True
            seen.add(i)
        return False


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "checkIfExist",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([10, 2, 5, 3])


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([7, 1, 14, 11])


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert not solution([3, 1, 7, 11])
