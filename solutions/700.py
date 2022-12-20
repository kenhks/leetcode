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

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val == val:
                return root
            elif root.val < val:
                return self.searchBST(root.right, val)
            else:
                return self.searchBST(root.left, val)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "searchBST",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([4, 2, 7, 1, 3])
    assert solution(root, val=2)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([4, 2, 7, 1, 3])
    assert not solution(root, val=5)
