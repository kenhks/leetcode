from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with two pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums) == 0:
            return ans
        left = right = nums[0]
        for n in nums[1:] + nums[:1]:
            if right + 1 == n:
                right = n
            else:
                if left == right:
                    ans.append(str(left))
                else:
                    ans.append(f"{left}->{right}")
                left = right = n
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "summaryRanges",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(nums=[]) == []
