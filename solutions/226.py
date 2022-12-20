from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, get_Tree_values, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.right, root.left = root.left, root.right
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "invertTree",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([4, 2, 7, 1, 3, 6, 9])
    actual = solution(root)
    assert get_Tree_values(actual) == [4, 7, 2, 9, 6, 3, 1]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([2, 1, 3])
    actual = solution(root)
    assert get_Tree_values(actual) == [2, 3, 1]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([])
    actual = solution(root)
    assert get_Tree_values(actual) == []
