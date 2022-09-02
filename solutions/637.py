from collections import deque
from typing import List, Optional

import pytest

from data_structures import TreeNode
from utils import create_Tree, parametrize_solution_cls


class Solution:
    """
    DFS, Convert tree to hashmap by level
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = maximum depth of tree
    """

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_map = {}

        def add_levels(node, level):
            if level in level_map:
                level_map[level].append(node.val)
            else:
                level_map[level] = [node.val]
            if node.left:
                add_levels(node.left, level + 1)
            if node.right:
                add_levels(node.right, level + 1)

        add_levels(root, 0)
        return [sum(j) / len(j) for j in level_map.values()]


class Solution2:
    """
    BFS, Convert tree to hashmap by level
    Time Complexity: O(n)
    Space Complexity: O(h)
    h = maximum depth of tree
    """

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        ans = []
        while q:
            q_size = len(q)
            level_sum = 0
            for _ in range(q_size):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level_sum / q_size)
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "averageOfLevels",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    root = create_Tree([3, 9, 20, None, None, 15, 7])
    assert solution(root) == pytest.approx([3, 14.5, 11], 0.01)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    root = create_Tree([3, 9, 20, 15, 7])
    assert solution(root) == pytest.approx([3, 14.5, 11], 0.01)
