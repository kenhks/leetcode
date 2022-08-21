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

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maxDepth",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([3, 9, 20, None, None, 15, 7])
    assert solution(root) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, None, 2])
    assert solution(root) == 2
