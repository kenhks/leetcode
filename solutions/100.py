from collections import deque
from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS, Recursive
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q


class Solution2:
    """
    BFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = True
        stack = deque([(p, q)])
        while stack:
            for _ in range(len(stack)):
                a, b = stack.popleft()
                if a and b:
                    if a.val != b.val:
                        ans = False
                    stack.append((a.left, b.left))
                    stack.append((a.right, b.right))
                elif a is None and b is None:
                    pass
                else:
                    ans = False
                if not ans:
                    break
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
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
