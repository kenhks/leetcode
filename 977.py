from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    left, right = 0, len(nums) - 1
    if nums[-1] <= 0:
        squares = [i ** 2 for i in nums[::-1]]
    elif nums[0] >= 0:
        squares = [i ** 2 for i in nums]
    else:
        squares = []
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                squares.insert(0, nums[left] ** 2)
                left += 1
            else:
                squares.insert(0, nums[right] ** 2)
                right -= 1
    return squares


def test_1():
    assert sortedSquares([-4, -1, 0, 3, 10],) == [0, 1, 9, 16, 100]


def test_2():
    assert sortedSquares([0],) == [0]


def test_3():
    assert sortedSquares([-4, -1, 0],) == [0, 1, 16]
