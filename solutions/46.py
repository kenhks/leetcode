from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Iterative
    Time Complexity: O(n!) =  (n!) * \\sum_{k=1}^{k=n-1} 1/((n-k)!) = ~= (n!e-1)
    Space Complexity: O(n!) = 2 * (n!) * \\sum_{k=1}^{k=n-1} 1/((n-k)!) ~= 2 * (n!e-1)
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        used_indexes = [set()]
        size = 0
        while size < len(nums):
            new_result = []
            new_used_indexes = []
            for i in range(len(result)):
                for j, n in enumerate(nums):
                    if j in used_indexes[i]:
                        continue
                    new_result.append(result[i] + [n])
                    new_used_index = used_indexes[i].copy()
                    new_used_index.add(j)
                    new_used_indexes.append(new_used_index)
            result = new_result
            used_indexes = new_used_indexes
            size += 1
        return result


class Solution2:
    """
    Recursive
    Time Complexity: O(n!)
    Space Complexity: O(n!)
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            m = nums[i]
            restl = nums[:i] + nums[i + 1 :]
            for p in self.permute(restl):
                result.append([m] + p)
        return result


class Solution3:
    """
    Iterative with stack
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = [(nums, [])]
        res = []
        while stack:
            nums, path = stack.pop()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i + 1 :]
                stack.append((newNums, path + [nums[i]]))
        return res


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "permute",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [1, 2, 3]
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sorted(solution(nums), key=lambda x: tuple(x)) == expected


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [0, 1]
    expected = [[0, 1], [1, 0]]
    assert sorted(solution(nums), key=lambda x: tuple(x)) == expected


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    nums = [1]
    expected = [[1]]
    assert sorted(solution(nums), key=lambda x: tuple(x)) == expected


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    nums = [1, 2, 3, 4]
    expected = [
        [1, 2, 3, 4],
        [1, 2, 4, 3],
        [1, 3, 2, 4],
        [1, 3, 4, 2],
        [1, 4, 2, 3],
        [1, 4, 3, 2],
        [2, 1, 3, 4],
        [2, 1, 4, 3],
        [2, 3, 1, 4],
        [2, 3, 4, 1],
        [2, 4, 1, 3],
        [2, 4, 3, 1],
        [3, 1, 2, 4],
        [3, 1, 4, 2],
        [3, 2, 1, 4],
        [3, 2, 4, 1],
        [3, 4, 1, 2],
        [3, 4, 2, 1],
        [4, 1, 2, 3],
        [4, 1, 3, 2],
        [4, 2, 1, 3],
        [4, 2, 3, 1],
        [4, 3, 1, 2],
        [4, 3, 2, 1],
    ]
    assert sorted(solution(nums), key=lambda x: tuple(x)) == expected


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    nums = [1, 2, 3, 4, 5]
    expected = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 5, 4],
        [1, 2, 4, 3, 5],
        [1, 2, 4, 5, 3],
        [1, 2, 5, 3, 4],
        [1, 2, 5, 4, 3],
        [1, 3, 2, 4, 5],
        [1, 3, 2, 5, 4],
        [1, 3, 4, 2, 5],
        [1, 3, 4, 5, 2],
        [1, 3, 5, 2, 4],
        [1, 3, 5, 4, 2],
        [1, 4, 2, 3, 5],
        [1, 4, 2, 5, 3],
        [1, 4, 3, 2, 5],
        [1, 4, 3, 5, 2],
        [1, 4, 5, 2, 3],
        [1, 4, 5, 3, 2],
        [1, 5, 2, 3, 4],
        [1, 5, 2, 4, 3],
        [1, 5, 3, 2, 4],
        [1, 5, 3, 4, 2],
        [1, 5, 4, 2, 3],
        [1, 5, 4, 3, 2],
        [2, 1, 3, 4, 5],
        [2, 1, 3, 5, 4],
        [2, 1, 4, 3, 5],
        [2, 1, 4, 5, 3],
        [2, 1, 5, 3, 4],
        [2, 1, 5, 4, 3],
        [2, 3, 1, 4, 5],
        [2, 3, 1, 5, 4],
        [2, 3, 4, 1, 5],
        [2, 3, 4, 5, 1],
        [2, 3, 5, 1, 4],
        [2, 3, 5, 4, 1],
        [2, 4, 1, 3, 5],
        [2, 4, 1, 5, 3],
        [2, 4, 3, 1, 5],
        [2, 4, 3, 5, 1],
        [2, 4, 5, 1, 3],
        [2, 4, 5, 3, 1],
        [2, 5, 1, 3, 4],
        [2, 5, 1, 4, 3],
        [2, 5, 3, 1, 4],
        [2, 5, 3, 4, 1],
        [2, 5, 4, 1, 3],
        [2, 5, 4, 3, 1],
        [3, 1, 2, 4, 5],
        [3, 1, 2, 5, 4],
        [3, 1, 4, 2, 5],
        [3, 1, 4, 5, 2],
        [3, 1, 5, 2, 4],
        [3, 1, 5, 4, 2],
        [3, 2, 1, 4, 5],
        [3, 2, 1, 5, 4],
        [3, 2, 4, 1, 5],
        [3, 2, 4, 5, 1],
        [3, 2, 5, 1, 4],
        [3, 2, 5, 4, 1],
        [3, 4, 1, 2, 5],
        [3, 4, 1, 5, 2],
        [3, 4, 2, 1, 5],
        [3, 4, 2, 5, 1],
        [3, 4, 5, 1, 2],
        [3, 4, 5, 2, 1],
        [3, 5, 1, 2, 4],
        [3, 5, 1, 4, 2],
        [3, 5, 2, 1, 4],
        [3, 5, 2, 4, 1],
        [3, 5, 4, 1, 2],
        [3, 5, 4, 2, 1],
        [4, 1, 2, 3, 5],
        [4, 1, 2, 5, 3],
        [4, 1, 3, 2, 5],
        [4, 1, 3, 5, 2],
        [4, 1, 5, 2, 3],
        [4, 1, 5, 3, 2],
        [4, 2, 1, 3, 5],
        [4, 2, 1, 5, 3],
        [4, 2, 3, 1, 5],
        [4, 2, 3, 5, 1],
        [4, 2, 5, 1, 3],
        [4, 2, 5, 3, 1],
        [4, 3, 1, 2, 5],
        [4, 3, 1, 5, 2],
        [4, 3, 2, 1, 5],
        [4, 3, 2, 5, 1],
        [4, 3, 5, 1, 2],
        [4, 3, 5, 2, 1],
        [4, 5, 1, 2, 3],
        [4, 5, 1, 3, 2],
        [4, 5, 2, 1, 3],
        [4, 5, 2, 3, 1],
        [4, 5, 3, 1, 2],
        [4, 5, 3, 2, 1],
        [5, 1, 2, 3, 4],
        [5, 1, 2, 4, 3],
        [5, 1, 3, 2, 4],
        [5, 1, 3, 4, 2],
        [5, 1, 4, 2, 3],
        [5, 1, 4, 3, 2],
        [5, 2, 1, 3, 4],
        [5, 2, 1, 4, 3],
        [5, 2, 3, 1, 4],
        [5, 2, 3, 4, 1],
        [5, 2, 4, 1, 3],
        [5, 2, 4, 3, 1],
        [5, 3, 1, 2, 4],
        [5, 3, 1, 4, 2],
        [5, 3, 2, 1, 4],
        [5, 3, 2, 4, 1],
        [5, 3, 4, 1, 2],
        [5, 3, 4, 2, 1],
        [5, 4, 1, 2, 3],
        [5, 4, 1, 3, 2],
        [5, 4, 2, 1, 3],
        [5, 4, 2, 3, 1],
        [5, 4, 3, 1, 2],
        [5, 4, 3, 2, 1],
    ]
    assert sorted(solution(nums), key=lambda x: tuple(x)) == expected
