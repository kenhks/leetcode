import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap for groupsize
    Time Complexity: O(nlog(10, n))
    Space Complexity: O(10log(10, n))
    """

    def countLargestGroup(self, n: int) -> int:
        digit_sum_map = {}
        for i in range(1, n + 1):
            digit_sum = 0
            while i > 0:
                i, d = divmod(i, 10)
                digit_sum += d
            digit_sum_map[digit_sum] = digit_sum_map.get(digit_sum, 0) + 1
        ans = 0
        max_size = 0
        for size in digit_sum_map.values():
            if size > max_size:
                max_size = size
                ans = 1
            elif size == max_size:
                ans += 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "countLargestGroup",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(n=13) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(n=2) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(n=100) == 1
