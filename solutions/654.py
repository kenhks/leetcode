from typing import List, Optional

import pytest

from data_structures import TreeNode
from utils import get_Tree_values, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_index, max_value = -1, -1
        for i, n in enumerate(nums):
            if n > max_value:
                max_index, max_value = i, n
        root = TreeNode(max_value)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1 :])
        return root


class Solution2:
    """
    DFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for n in nums:
            node = TreeNode(n)
            while stack and n > stack[-1].val:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "constructMaximumBinaryTree",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums = [3, 2, 1, 6, 0, 5]
    assert get_Tree_values(solution(nums)) == [6, 3, 5, None, 2, 0, None, None, 1]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums = [3, 2, 1]
    assert get_Tree_values(solution(nums)) == [3, None, 2, None, 1]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    nums = [1]
    assert get_Tree_values(solution(nums)) == [1]
