from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = {}
        for i in nums:
            if i in nums_set:
                return True
            else:
                nums_set[i] = True
        return False


def test_1():
    assert Solution().containsDuplicate([1, 2, 3, 1]) == True


def test_2():
    assert Solution().containsDuplicate([1, 2, 3, 4]) == False


def test_3():
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True


def test_4():
    assert Solution2().containsDuplicate([1, 2, 3, 1]) == True


def test_5():
    assert Solution2().containsDuplicate([1, 2, 3, 4]) == False


def test_6():
    assert Solution2().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
