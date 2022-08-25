import pytest

from utils import parametrize_solution_cls

MOCK_TARGET = f"{__name__}.get_answer"


def get_answer():
    pass


def guess(n):
    """
    @return -1 if num is higher than the picked number
             1 if num is lower than the picked number
             otherwise return 0
    """
    if n == get_answer():
        return 0
    elif n > get_answer():
        return -1
    else:
        return 1


class Solution:
    """
    Binary search
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            guess_mid = guess(mid)
            if guess_mid == 0:
                return mid
            elif guess_mid == 1:
                l = mid + 1
            elif guess_mid == -1:
                r = mid - 1
        return r


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "guessNumber",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(mocker, solution):
    pick = 6
    mocker.patch(MOCK_TARGET, return_value=pick)
    assert solution(10) == pick


@pytest.mark.parametrize("solution", solutions)
def test_2(mocker, solution):
    pick = 1
    mocker.patch(MOCK_TARGET, return_value=pick)
    assert solution(1) == pick


@pytest.mark.parametrize("solution", solutions)
def test_3(mocker, solution):
    pick = 1
    mocker.patch(MOCK_TARGET, return_value=pick)
    assert solution(2) == pick
