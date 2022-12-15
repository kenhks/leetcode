from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Recursive
    Time Complexity: O(n!)
    Space Complexity: O(n!)
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        ans.add(tuple())

        def dfs(sub_nums):
            ans.add(tuple(sub_nums))
            if len(sub_nums) > 1:
                for i in range(len(sub_nums)):
                    dfs(sub_nums[:i] + sub_nums[i + 1 :])

        dfs(nums)
        return [list(i) for i in ans]


class Solution2:
    """
    Cascading
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n * 2^n)
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            ans += [curr + [num] for curr in ans]
        return ans


class Solution3:
    """
    Bitmasking
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n * 2^n)
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        start = 2**n
        end = start * 2
        for i in range(start, end):
            bitmask = bin(i)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] == "1"])
        return output


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "subsets",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    expected = [
        [],
        [1],
        [2],
        [1, 2],
        [3],
        [1, 3],
        [2, 3],
        [1, 2, 3],
    ]
    assert set(tuple(i) for i in solution([1, 2, 3])) == set(tuple(i) for i in expected)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    expected = [[], [0]]
    assert set(tuple(i) for i in solution([0])) == set(tuple(i) for i in expected)
