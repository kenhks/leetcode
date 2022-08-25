import pytest

from utils import parametrize_solution_cls

MOCK_TARGET = f"{__name__}.bad_version"


def bad_version():
    pass


def isBadVersion(n):
    return n >= bad_version()


class Solution:
    """
    Binary search
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "firstBadVersion",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(mocker, solution):
    bad_version = 4
    mocker.patch(MOCK_TARGET, return_value=bad_version)
    assert solution(5) == bad_version


@pytest.mark.parametrize("solution", solutions)
def test_2(mocker, solution):
    bad_version = 1
    mocker.patch(MOCK_TARGET, return_value=bad_version)
    assert solution(1) == bad_version
