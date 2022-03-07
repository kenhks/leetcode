from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, count = 0, 0
        while i < len(nums):
            if nums[i] == 0:
                count += 1
                nums.pop(i)
            else:
                i += 1
        nums += [0] * count


class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_nonzero = 0
        for cur, i in enumerate(nums):
            if i != 0:
                nums[next_nonzero], nums[cur] = nums[cur], nums[next_nonzero]
                next_nonzero += 1

def test_1():
    l = [0, 1, 0, 3, 12]
    Solution2().moveZeroes(l)
    print(l)
    assert l == [1, 3, 12, 0, 0]
