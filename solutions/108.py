from collections import deque
from typing import List, Optional

import pytest

from data_structures import TreeNode
from utils import get_Tree_values, parametrize_solution_cls


class Solution:
    """
    Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1 :])
            return root


class Solution2:
    """
    Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) > 0:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            stack = deque([(0, mid, mid + 1, len(nums), root)])
            while stack:
                for _ in range(len(stack)):
                    left_start, left_end, right_start, right_end, parent = stack.pop()
                    if left_start < left_end:
                        left_mid = (left_start + left_end) // 2
                        parent.left = left_node = TreeNode(nums[left_mid])
                        stack.append((left_start, left_mid, left_mid + 1, left_end, left_node))
                    if right_start < right_end:
                        right_mid = (right_start + right_end) // 2
                        parent.right = right_node = TreeNode(nums[right_mid])
                        stack.append((right_start, right_mid, right_mid + 1, right_end, right_node))
            return root


solutions = parametrize_solution_cls(
    [
        # Solution,
        Solution2,
    ],
    "sortedArrayToBST",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [-10, -3, 0, 5, 9]
    assert get_Tree_values(solution(nums)) == [0, -3, 9, -10, None, 5]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [1, 3]
    assert get_Tree_values(solution(nums)) == [3, 1]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    nums = [1, 2, 3, 4, 5, 6, 7]
    assert get_Tree_values(solution(nums)) == [4, 2, 6, 1, 3, 5, 7]
