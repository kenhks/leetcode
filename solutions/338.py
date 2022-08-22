from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Count number from number
    Time Complexity: O(nlog(2, n)) = nlog(2, n)
    Space Complexity: O(1)
    """

    def countBits(self, n: int) -> List[int]:
        return [f"{i:b}".count("1") for i in range(n + 1)]


class Solution2:
    """
    DP with array, use increasing offset
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset << 1 == i:
                offset = i
            result[i] = 1 + result[i - offset]
        return result


class Solution3:
    """
    DP with array, use half number
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            if i & 1 == 1:
                result[i] = 1 + result[i // 2]
            else:
                result[i] = result[i // 2]
        return result


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "countBits",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(2) == [0, 1, 1]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(5) == [0, 1, 1, 2, 1, 2]
