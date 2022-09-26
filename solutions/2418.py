from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sort combined list
    Time Complexity: O(n) = 2n
    Space Complexity: O(n)
    """

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [i for i, j in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "sortPeople",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    names = ["Mary", "John", "Emma"]
    heights = [180, 165, 170]
    assert solution(names, heights) == ["Mary", "Emma", "John"]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]
    assert solution(names, heights) == ["Bob", "Alice", "Bob"]
