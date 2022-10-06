from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS with recursion
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter: int = 0

        def dfs(node):
            nonlocal max_diameter
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            max_diameter = max(max_diameter, left + right)
            return 1 + max(left, right)

        dfs(root)
        return max_diameter


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "diameterOfBinaryTree",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, 2, 3, 4, 5])
    assert solution(root) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, 2])
    assert solution(root) == 1
