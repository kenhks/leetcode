from typing import List, Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    BFS
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        level_nodes = [root] if root else []
        while level_nodes:
            level_val = []
            new_level_nodes = []
            for node in level_nodes:
                level_val.append(node.val)
                if node.left:
                    new_level_nodes.append(node.left)
                if node.right:
                    new_level_nodes.append(node.right)
            level_nodes = new_level_nodes
            ans.append(level_val)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "preorderTraversal",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([3, 9, 20, None, None, 15, 7])
    assert solution(root) == [[3], [9, 20], [15, 7]]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1])
    assert solution(root) == [[1]]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([])
    assert solution(root) == []
