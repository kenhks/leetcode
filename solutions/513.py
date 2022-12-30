from collections import deque
from typing import List, Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    BFS, Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> List[int]:
        ans = None
        stack = deque([root]) if root else []
        while stack:
            ans = stack[0].val
            for _ in range(len(stack)):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findBottomLeftValue",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([2, 1, 3])
    assert solution(root) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, 2, 3, 4, None, 5, 6, None, None, 7])
    assert solution(root) == 7
