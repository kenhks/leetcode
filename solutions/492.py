import math
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Math
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    """

    def constructRectangle(self, area: int) -> List[int]:
        ans = [area, 1]
        for i in range(math.ceil(math.sqrt(area)), 0, -1):
            d, r = divmod(area, i)
            if r == 0:
                ans = [max(i, d), min(i, d)]
                break
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "constructRectangle",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(area=4) == [2, 2]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(area=37) == [37, 1]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(122122) == [427, 286]
