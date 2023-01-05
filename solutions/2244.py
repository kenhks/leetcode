from collections import Counter
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def minimumRounds(self, tasks: List[int]) -> int:
        level_counter = Counter(tasks)
        ans = 0
        for count in level_counter.values():
            if count == 1:
                ans = -1
                break
            round_count, count = divmod(count, 3)
            if count:
                round_count += 1
            ans += round_count
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "minimumRounds",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
    assert solution(tasks) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    tasks = [2, 3, 3]
    assert solution(tasks) == -1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    tasks = [5, 5, 5, 5]
    assert solution(tasks) == 2
