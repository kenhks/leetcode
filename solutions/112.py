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

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        else:
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
                root.right, targetSum - root.val
            )


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "hasPathSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    assert solution(root, 22)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, 2, 3])
    assert not solution(root, 5)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([])
    assert not solution(root, 0)
