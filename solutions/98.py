from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], min_value, max_value) -> bool:
            if not node:
                return True
            if node.val <= min_value or node.val >= max_value:
                return False
            return dfs(node.left, min_value, node.val) and dfs(node.right, node.val, max_value)

        return dfs(root, float("-inf"), float("inf"))


class Solution2:
    """
    BFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float("-inf"), float("inf"))] if root else []
        ans = True
        while stack and ans:
            new_stack = []
            for node, min_value, max_value in stack:
                if node.val <= min_value or node.val >= max_value:
                    ans = False
                    break
                if node.left:
                    new_stack.append((node.left, min_value, node.val))
                if node.right:
                    new_stack.append((node.right, node.val, max_value))
            stack = new_stack
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "isValidBST",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([2, 1, 3])
    assert solution(root)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([5, 1, 4, None, None, 3, 6])
    assert not solution(root)
