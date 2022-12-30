import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap
    Time Complexity: O(n)
    Space Complexity: O(1) = 6
    """

    def maxNumberOfBalloons(self, text: str) -> int:
        s = set("balloon")
        counter = {i: 0 for i in s}
        for c in text:
            if c in s:
                counter[c] += 1
        counter["l"] //= 2
        counter["o"] //= 2
        return min(counter.values())


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maxNumberOfBalloons",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(text="nlaebolko") == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(text="loonbalxballpoon") == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(text="leetcode") == 0
