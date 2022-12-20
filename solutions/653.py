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

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ans = False
        seen = set()

        def dfs(node: TreeNode):
            nonlocal ans
            if k - node.val not in seen:
                seen.add(node.val)
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
            else:
                ans = True

        if root:
            dfs(root)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findTarget",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([5, 3, 6, 2, 4, None, 7])
    assert solution(root, k=9)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([5, 3, 6, 2, 4, None, 7])
    assert not solution(root, k=28)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([])
    assert not solution(root, k=1)
