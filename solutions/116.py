from typing import Optional

import pytest

from data_structures import TreeNode2
from utils import (
    create_Tree,
    get_perfect_BinaryTree_next_values,
    parametrize_solution_cls,
)


class Solution:
    """
    BFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def connect(self, root: Optional[TreeNode2]) -> Optional[TreeNode2]:
        if root:
            level_nodes = [root]
            while level_nodes:
                new_level_nodes = []
                for i, node in enumerate(level_nodes):
                    if i > 0:
                        level_nodes[i - 1].next = node
                    if node.left:
                        new_level_nodes.append(node.left)
                    if node.right:
                        new_level_nodes.append(node.right)
                level_nodes = new_level_nodes
        return root


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "connect",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, 2, 3, 4, 5, 6, 7], node_cls=TreeNode2)
    solution(root)
    assert get_perfect_BinaryTree_next_values(root) == [1, None, 2, 3, None, 4, 5, 6, 7, None]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([], node_cls=TreeNode2)
    solution(root)
    assert get_perfect_BinaryTree_next_values(root) == []
