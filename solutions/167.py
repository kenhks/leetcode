from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            c_target = numbers[l] + numbers[r]
            if c_target == target:
                return [l + 1, r + 1]
            elif c_target > target:
                r -= 1
            elif c_target < target:
                l += 1


def test_1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]


def test_2():
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]


def test_3():
    assert Solution().twoSum([-1, 0], -1) == [1, 2]
