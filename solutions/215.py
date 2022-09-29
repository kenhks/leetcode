import heapq
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Remove max value (k - 1) times
    Time Complexity: O(kn) = 2kn -n
    Space Complexity: O(1)
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        while k > 1:
            nums.remove(max(nums))
            k -= 1
        return max(nums)


class Solution2:
    """
    Sort the array
    Time Complexity: O(nlog(2, n)) = nlog(2, n)  + 2n
    Space Complexity: O(1)
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


class Solution3:
    """
    Heap
    Time Complexity: O(n + klog(2, n))
    Space Complexity: O(1)
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "findKthLargest",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [3, 2, 1, 5, 6, 4]
    assert solution(nums, k=2) == 5


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    assert solution(nums, k=4) == 4


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    nums = [1]
    assert solution(nums, k=1) == 1
