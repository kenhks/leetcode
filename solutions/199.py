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

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = deque([root]) if root else []
        while stack:
            ans.append(stack[-1].val)
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
    "rightSideView",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, 2, 3, None, 5, None, 4])
    assert solution(root) == [1, 3, 4]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, None, 3])
    assert solution(root) == [1, 3]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([])
    assert solution(root) == []


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    root = create_Tree([1, 2, 3, 4])
    assert solution(root) == [1, 3, 4]
