from typing import List


def search(nums: List[int], target: int) -> int:
    index = -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            index = mid
            break
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return index


def test_1():
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4


def test_2():
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
