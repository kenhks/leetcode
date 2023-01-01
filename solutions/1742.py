from collections import defaultdict

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap for digit sum counter
    Time Complexity: O(nlog(10, n)) = 2nlog(10, n)
    Space Complexity: O(n)
    """

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans = 0
        box_counter = defaultdict(int)
        for n in range(lowLimit, highLimit + 1):
            box_number = sum(int(i) for i in str(n))
            box_counter[box_number] += 1
            ans = max(box_counter[box_number], ans)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "countBalls",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(lowLimit=1, highLimit=10) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(lowLimit=5, highLimit=15) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(lowLimit=19, highLimit=28) == 2
