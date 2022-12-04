import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Iterative
    Time Complexity: O(log(max(x, y)))
    Space Complexity: O(1)
    """

    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x > 0 or y > 0:
            if (x & 1) != (y & 1):
                ans += 1
            x = x >> 1
            y = y >> 1
        return ans


class Solution2:
    """
    Iterative
    Time Complexity: O(log(max(x, y)))
    Space Complexity: O(1)
    """

    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        num = x ^ y
        while num > 0:
            count += num & 1
            num = num >> 1
        return count


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "hammingDistance",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(x=1, y=4) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(x=3, y=1) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(x=0, y=7) == 3
