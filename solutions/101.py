from collections import deque
from typing import Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    Iterative, BFS with queue
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans: bool = True
        if root:
            q = deque([(root.left, root.right)])
            while q:
                l, r = q.popleft()
                if l and r and l.val == r.val:
                    q.extend([(l.right, r.left), (l.left, r.right)])
                elif l is r:
                    continue
                else:
                    ans = False
                    break
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "isSymmetric",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, 2, 2, 3, 4, 4, 3])
    assert solution(root)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, 2, 2, None, 3, None, 3])
    assert not solution(root)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([1])
    assert solution(root)
