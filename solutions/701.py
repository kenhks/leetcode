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

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "insertIntoBST",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([4, 2, 7, 1, 3])
    actual = solution(root, val=5)
    assert get_Tree_values(actual) == [4, 2, 7, 1, 3, 5]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([40, 20, 60, 10, 30, 50, 70])
    actual = solution(root, val=25)
    assert get_Tree_values(actual) == [40, 20, 60, 10, 30, 50, 70, None, None, 25]
