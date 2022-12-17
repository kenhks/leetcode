from typing import List, Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    BFS
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        level_nodes = [root] if root else []
        while level_nodes:
            next_level_nodes = []
            level_max = level_nodes[0].val
            for n in level_nodes:
                if n.left:
                    next_level_nodes.append(n.left)
                if n.right:
                    next_level_nodes.append(n.right)
                level_max = max(n.val, level_max)
            ans.append(level_max)
            level_nodes = next_level_nodes
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "largestValues",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([1, 3, 2, 5, 3, None, 9])
    assert solution(root) == [1, 3, 9]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([1, 2, 3])
    assert solution(root) == [1, 3]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    root = create_Tree([1])
    assert solution(root) == [1]
