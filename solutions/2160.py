import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(log(10, n)) = 3log(10, n)
    Space Complexity: O(log(10, n))
    """

    def minimumSum(self, num: int) -> int:
        nums = []
        while num > 0:
            num, d = divmod(num, 10)
            nums.append(d)
        nums.sort()
        return sum(nums[:2]) * 10 + sum(nums[-2:])


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "minimumSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(num=2932) == 52


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(num=4009) == 13
