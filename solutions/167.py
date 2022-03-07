from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            c_target = numbers[l] + numbers[r]
            if c_target < target:
                l += 1
            elif c_target > target:
                r -= 1
            else:
                return [l + 1, r + 1]


class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(numbers, start=1):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

def test_1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]


def test_2():
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]


def test_3():
    assert Solution().twoSum([-1, 0], -1) == [1, 2]


def test_4():
    assert Solution2().twoSum([2, 7, 11, 15], 9) == [1, 2]


def test_5():
    assert Solution2().twoSum([2, 3, 4], 6) == [1, 3]


def test_6():
    assert Solution2().twoSum([-1, 0], -1) == [1, 2]
