from typing import List, Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node: TreeNode):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            ans.append(node.val)

        if root:
            dfs(root)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "postorderTraversal",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, None, 2, 3])
    assert solution(root) == [3, 2, 1]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([])
    assert solution(root) == []


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([1])
    assert solution(root) == [1]
