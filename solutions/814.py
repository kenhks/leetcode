from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, get_Tree_values, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode) -> bool:
            left_delete = dfs(node.left) if node.left else True
            right_delete = dfs(node.right) if node.right else True
            if left_delete:
                node.left = None
            if right_delete:
                node.right = None
            return node.val == 0 and left_delete and right_delete

        if root and not dfs(root):
            return root
        return None


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "pruneTree",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, None, 0, 0, 1])
    assert get_Tree_values(solution(root)) == [1, None, 0, None, 1]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, 0, 1, 0, 0, 0, 1])
    assert get_Tree_values(solution(root)) == [1, None, 1, None, 1]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([1, 1, 0, 1, 1, 0, 1, 0])
    assert get_Tree_values(solution(root)) == [1, 1, 0, 1, 1, None, 1]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    root = create_Tree([1, 1, 1])
    assert get_Tree_values(solution(root)) == [1, 1, 1]
