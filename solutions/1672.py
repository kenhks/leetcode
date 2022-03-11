from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(ac) for ac in accounts)


def test_1():
    accounts = [[1, 2, 3], [3, 2, 1]]
    assert Solution().maximumWealth(accounts) == 6


def test_2():
    accounts = [[1, 5], [7, 3], [3, 5]]
    assert Solution().maximumWealth(accounts) == 10


def test_3():
    accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    assert Solution().maximumWealth(accounts) == 17
