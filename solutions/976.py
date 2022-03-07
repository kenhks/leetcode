from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if a < b + c:
                return a + b + c
        return 0


def test_1():
    assert Solution().largestPerimeter([2, 1, 2]) == 5


def test_2():
    assert Solution().largestPerimeter([1, 2, 1]) == 0
