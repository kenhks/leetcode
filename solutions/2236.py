from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return (root.left.val + root.right.val) == root.val


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "checkTree",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([10, 4, 6])
    assert solution(root)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([5, 3, 1])
    assert not solution(root)
