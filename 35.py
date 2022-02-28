from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    if target < nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    else:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
    return left


def test_1():
    assert searchInsert([1, 3, 5, 6], 5) == 2


def test_2():
    assert searchInsert([1, 3, 5, 6], 2) == 1


def test_3():
    assert searchInsert([1, 3, 5, 6], 7) == 4
