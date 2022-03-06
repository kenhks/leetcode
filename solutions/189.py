from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        k = k % len(nums)
        if k == 0:
            return
        nums[:-k], nums[-k:] = nums[-k:], nums[:-k]


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)


def test_1():
    l = [1, 2, 3, 4, 5, 6, 7]
    Solution2().rotate(l, 3)
    assert l == [5, 6, 7, 1, 2, 3, 4]


def test_2():
    l = [-1, -100, 3, 99]
    Solution2().rotate(l, 2)
    assert l == [3, 99, -1, -100]
