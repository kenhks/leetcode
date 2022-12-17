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

    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            if node.left and node.right:
                return 1 + min(dfs(node.left), dfs(node.right))
            elif node.left:
                return 1 + dfs(node.left)
            elif node.right:
                return 1 + dfs(node.right)
            else:
                return 1

        return dfs(root)


class Solution2:
    """
    BFS
    Time Complexity: O(n)
    Space Complexity: O(n)
    h = height of tree ~= log(2, n)
    """

    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        level_nodes = [root] if root else []
        while level_nodes:
            depth += 1
            next_level_nodes = []
            for node in level_nodes:
                if not node.left and not node.right:
                    next_level_nodes.clear()
                    break
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            level_nodes = next_level_nodes
        return depth


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "minDepth",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([3, 9, 20, None, None, 15, 7])
    assert solution(root) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([2, None, 3, None, 4, None, 5, None, 6])
    assert solution(root) == 5


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([1])
    assert solution(root) == 1
