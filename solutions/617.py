from typing import List, Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, get_Tree_values, parametrize_solution_cls


class Solution:
    """
    DFS
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2) -> TreeNode:
            if node1 and node2:
                new = TreeNode(node1.val + node2.val)
                new.left = dfs(node1.left, node2.left)
                new.right = dfs(node1.right, node2.right)
                return new
            else:
                return node1 or node2

        return dfs(root1, root2)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "mergeTrees",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root1 = create_Tree([1, 3, 2, 5])
    root2 = create_Tree([2, 1, 3, None, 4, None, 7])
    assert get_Tree_values(solution(root1, root2)) == [3, 4, 5, 5, 4, None, 7]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root1 = create_Tree([1])
    root2 = create_Tree([1, 2])
    assert get_Tree_values(solution(root1, root2)) == [2, 2, None]
