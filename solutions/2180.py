import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(nlog(10, n))
    Space Complexity: O(1)
    """

    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            if sum(int(j) for j in str(i)) % 2 == 0:
                count += 1
        return count


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "countEven",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(num=4) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(num=30) == 14


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution()
