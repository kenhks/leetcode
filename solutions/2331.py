from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = height of tree ~= log(2, n)
    """

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "evaluateTree",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([2, 1, 3, None, None, 0, 1])
    assert solution(root)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([0])
    assert not solution(root)
