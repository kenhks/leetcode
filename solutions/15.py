from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashed without sort
    Time Complexity: O(nlogn + n^2)
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i, x in enumerate(nums[:-2]):
            freq = {}
            target = -x
            sub_result = []
            for y in nums[i + 1 :]:
                z = target - y
                if z in freq:
                    sub_result.append((y, z))
                if y not in freq:
                    freq[y] = 1
                else:
                    freq[y] += 1
            for r in sub_result:
                result.add(tuple(sorted((x,) + r)))
        return [list(i) for i in result]


class Solution2:
    """
    Hashed with sort
    Time Complexity: O(nlogn + n^2)
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, x in enumerate(nums[:-2]):
            if i == 0 and x > 0:
                break
            if i >= 1 and x == nums[i - 1]:
                continue
            checked = set()
            sub_result = set()
            for y in nums[i + 1 :]:
                z = -x - y
                if z in checked:
                    sub_result.add((z, y))
                checked.add(y)
            for r in sub_result:
                result.append([x] + list(r))
        return result


class Solution3:
    """
    Two pointer with sort
    Time Complexity: O(nlogn + n^2)
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, x in enumerate(nums[:-2]):
            if i == 0 and x > 0:
                break
            if i >= 1 and x == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            sub_result = set()
            while left < right:
                y, z = nums[left], nums[right]
                c_sum = x + y + z
                if c_sum == 0:
                    sub_result.add((y, z))
                    left += 1
                    right -= 1
                elif c_sum > 0:
                    right -= 1
                elif c_sum < 0:
                    left += 1
            for r in sub_result:
                result.append([x] + list(r))
        return result


class Solution4:
    """
    Brute Force:
    Time Complexity: O(n^3)
    Space Complexity: O(1)
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return [list(x) for x in triplets]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
        Solution4,
    ],
    "threeSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert sorted(solution([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert sorted(solution([0, 1, 1])) == []


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert sorted(solution([0, 0, 0])) == [[0, 0, 0]]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert sorted(solution([0, 0, 0, 0])) == [[0, 0, 0]]
