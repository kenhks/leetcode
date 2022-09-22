from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    BFS with hashmap
    Time Complexity: O(amount * n)
    Space Complexity: O(amount) = amount + 1
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        for a in range(1, amount + 1):
            for c in coins:
                if a < c:
                    continue
                dp[a] = min(dp.get(a, amount + 1), dp.get(a - c, amount + 1) + 1)
        if amount in dp:
            return dp[amount] if dp[amount] != amount + 1 else -1
        else:
            return -1


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "coinChange",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(coins=[1, 2, 5], amount=11) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(coins=[2], amount=3) == -1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(coins=[1], amount=0) == 0


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(coins=[186, 419, 83, 408], amount=6249) == 20
