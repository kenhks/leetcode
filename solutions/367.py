import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Binary search
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        root_left, root_right = 1, num // 2
        while root_left <= root_right:
            root_mid = (root_left + root_right) // 2
            root_mid_square = root_mid * root_mid
            if root_mid_square == num:
                return True
            elif root_mid_square < num:
                root_left = root_mid + 1
            else:
                root_right = root_mid - 1
        return False


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isPerfectSquare",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(16)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(14)
