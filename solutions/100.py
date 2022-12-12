from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    Recursive
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isSameTree",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    p = create_Tree([1, 2, 3])
    q = create_Tree([1, 2, 3])
    assert solution(p, q)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    p = create_Tree([1, 2])
    q = create_Tree([1, None, 2])
    assert not solution(p, q)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    p = create_Tree([1, 2, 1])
    q = create_Tree([1, 1, 2])
    assert not solution(p, q)
