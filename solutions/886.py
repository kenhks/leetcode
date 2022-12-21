from collections import defaultdict, deque
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Disjoint hashset
    Time Complexity: O(m^2 log(2, m)) = m^2log(2, m) + m^2
    Space Complexity: O(m)
    m = len(dislikes)
    """

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        possible = True
        group_a, group_b = set(), set()
        if dislikes:
            dislikes = sorted(dislikes, key=lambda x: tuple(x))
        while possible and dislikes:
            new_dislikes = []
            for a, b in dislikes:
                if a in group_a:
                    if b in group_a:
                        possible = False
                        break
                    else:
                        group_b.add(b)
                elif a in group_b:
                    if b in group_b:
                        possible = False
                        break
                    else:
                        group_a.add(b)
                elif b in group_a:
                    group_b.add(a)
                elif b in group_b:
                    group_a.add(a)
                else:
                    if not group_a and not group_b:
                        group_a.add(a)
                        group_b.add(b)
                    else:
                        new_dislikes.append([a, b])
            if len(dislikes) == len(new_dislikes):
                break
            dislikes = new_dislikes
        if possible and dislikes:
            possible = self.possibleBipartition(n - len(group_a) - len(group_b), dislikes)
        return possible


class Solution2:
    """
    Graph
    Time Complexity:  O(V + E)
    Space Complexity:  O(V + E)
    """

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        d = deque([])
        colors = {}
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        for i in graph.keys():
            if i not in colors:
                colors[i] = 1
                d.append(i)
                while d:
                    item = d.popleft()
                    for ch in graph[item]:
                        if ch in colors:
                            if colors[ch] == colors[item]:
                                return False
                        else:
                            colors[ch] = 1 - colors[item]
                            d.append(ch)
        return True


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "possibleBipartition",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    n = 4
    dislike = [[1, 2], [1, 3], [2, 4]]
    assert solution(n, dislike)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    n = 3
    dislike = [[1, 2], [1, 3], [2, 3]]
    assert not solution(n, dislike)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    n = 5
    dislike = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    assert not solution(n, dislike)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    n = 1
    dislike = []
    assert solution(n, dislike)


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    n = 5
    dislike = [[1, 2], [3, 4], [4, 5], [3, 5]]
    assert not solution(n, dislike)


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    n = 10
    dislike = [
        [5, 9],
        [5, 10],
        [5, 6],
        [5, 7],
        [1, 5],
        [4, 5],
        [2, 5],
        [5, 8],
        [3, 5],
    ]
    assert solution(n, dislike)


@pytest.mark.parametrize("solution", solutions)
def test_7(solution):
    n = 6
    dislike = [
        [1, 2],
        [1, 3],
        [3, 4],
        [4, 5],
    ]
    assert solution(n, dislike)


@pytest.mark.parametrize("solution", solutions)
def test_8(solution):
    n = 10
    dislike = [
        [4, 7],
        [4, 8],
        [5, 6],
        [1, 6],
        [3, 7],
        [2, 5],
        [5, 8],
        [1, 2],
        [4, 9],
        [6, 10],
        [8, 10],
        [3, 6],
        [2, 10],
        [9, 10],
        [3, 9],
        [2, 3],
        [1, 9],
        [4, 6],
        [5, 7],
        [3, 8],
        [1, 8],
        [1, 7],
        [2, 4],
    ]
    assert solution(n, dislike)


@pytest.mark.parametrize("solution", solutions)
def test_9(solution):
    n = 10
    dislike = [
        [4, 7],
        [4, 8],
        [5, 6],
        [1, 6],
        [3, 7],
        [2, 5],
        [5, 8],
        [1, 2],
        [4, 9],
        [6, 10],
        [8, 10],
        [3, 6],
        [2, 10],
        [9, 10],
        [3, 9],
        [2, 3],
        [1, 9],
        [4, 6],
        [5, 7],
        [3, 8],
        [1, 8],
        [1, 7],
        [2, 4],
    ]
    assert solution(n, dislike)


@pytest.mark.parametrize("solution", solutions)
def test_10(solution):
    n = 50
    dislike = [
        [21, 47],
        [4, 41],
        [2, 41],
        [36, 42],
        [32, 45],
        [26, 28],
        [32, 44],
        [5, 41],
        [29, 44],
        [10, 46],
        [1, 6],
        [7, 42],
        [46, 49],
        [17, 46],
        [32, 35],
        [11, 48],
        [37, 48],
        [37, 43],
        [8, 41],
        [16, 22],
        [41, 43],
        [11, 27],
        [22, 44],
        [22, 28],
        [18, 37],
        [5, 11],
        [18, 46],
        [22, 48],
        [1, 17],
        [2, 32],
        [21, 37],
        [7, 22],
        [23, 41],
        [30, 39],
        [6, 41],
        [10, 22],
        [36, 41],
        [22, 25],
        [1, 12],
        [2, 11],
        [45, 46],
        [2, 22],
        [1, 38],
        [47, 50],
        [11, 15],
        [2, 37],
        [1, 43],
        [30, 45],
        [4, 32],
        [28, 37],
        [1, 21],
        [23, 37],
        [5, 37],
        [29, 40],
        [6, 42],
        [3, 11],
        [40, 42],
        [26, 49],
        [41, 50],
        [13, 41],
        [20, 47],
        [15, 26],
        [47, 49],
        [5, 30],
        [4, 42],
        [10, 30],
        [6, 29],
        [20, 42],
        [4, 37],
        [28, 42],
        [1, 16],
        [8, 32],
        [16, 29],
        [31, 47],
        [15, 47],
        [1, 5],
        [7, 37],
        [14, 47],
        [30, 48],
        [1, 10],
        [26, 43],
        [15, 46],
        [42, 45],
        [18, 42],
        [25, 42],
        [38, 41],
        [32, 39],
        [6, 30],
        [29, 33],
        [34, 37],
        [26, 38],
        [3, 22],
        [18, 47],
        [42, 48],
        [22, 49],
        [26, 34],
        [22, 36],
        [29, 36],
        [11, 25],
        [41, 44],
        [6, 46],
        [13, 22],
        [11, 16],
        [10, 37],
        [42, 43],
        [12, 32],
        [1, 48],
        [26, 40],
        [22, 50],
        [17, 26],
        [4, 22],
        [11, 14],
        [26, 39],
        [7, 11],
        [23, 26],
        [1, 20],
        [32, 33],
        [30, 33],
        [1, 25],
        [2, 30],
        [2, 46],
        [26, 45],
        [47, 48],
        [5, 29],
        [3, 37],
        [22, 34],
        [20, 22],
        [9, 47],
        [1, 4],
        [36, 46],
        [30, 49],
        [1, 9],
        [3, 26],
        [25, 41],
        [14, 29],
        [1, 35],
        [23, 42],
        [21, 32],
        [24, 46],
        [3, 32],
        [9, 42],
        [33, 37],
        [7, 30],
        [29, 45],
        [27, 30],
        [1, 7],
        [33, 42],
        [17, 47],
        [12, 47],
        [19, 41],
        [3, 42],
        [24, 26],
        [20, 29],
        [11, 23],
        [22, 40],
        [9, 37],
        [31, 32],
        [23, 46],
        [11, 38],
        [27, 29],
        [17, 37],
        [23, 30],
        [14, 42],
        [28, 30],
        [29, 31],
        [1, 8],
        [1, 36],
        [42, 50],
        [21, 41],
        [11, 18],
        [39, 41],
        [32, 34],
        [6, 37],
        [30, 38],
        [21, 46],
        [16, 37],
        [22, 24],
        [17, 32],
        [23, 29],
        [3, 30],
        [8, 30],
        [41, 48],
        [1, 39],
        [8, 47],
        [30, 44],
        [9, 46],
        [22, 45],
        [7, 26],
        [35, 42],
        [1, 27],
        [17, 30],
        [20, 46],
        [18, 29],
        [3, 29],
        [4, 30],
        [3, 46],
    ]
    assert solution(n, dislike)


@pytest.mark.parametrize("solution", solutions)
def test_11(solution):
    n = 10
    dislike = [[1, 2], [3, 4], [5, 6], [6, 7], [8, 9], [7, 8]]
    assert solution(n, dislike)


@pytest.mark.parametrize("solution", solutions)
def test_12(solution):
    n = 50
    dislike = [
        [38, 50],
        [7, 12],
        [7, 49],
        [28, 41],
        [26, 28],
        [33, 36],
        [10, 12],
        [31, 44],
        [34, 35],
        [33, 41],
        [8, 41],
        [2, 5],
        [16, 19],
        [10, 34],
        [11, 48],
        [46, 48],
        [30, 31],
        [44, 45],
        [24, 27],
        [4, 8],
        [45, 48],
        [33, 50],
        [30, 42],
        [28, 46],
        [9, 36],
        [17, 23],
        [7, 28],
        [35, 36],
        [23, 25],
        [14, 43],
        [37, 41],
        [18, 35],
        [24, 39],
        [37, 38],
        [36, 50],
        [10, 13],
        [44, 50],
        [1, 35],
        [21, 37],
        [23, 38],
        [22, 42],
        [30, 39],
        [35, 46],
        [16, 38],
        [40, 48],
        [34, 41],
        [8, 12],
        [4, 15],
        [19, 43],
        [12, 50],
        [19, 34],
        [27, 49],
        [26, 43],
        [20, 37],
        [46, 47],
        [48, 50],
        [24, 48],
        [7, 21],
        [40, 45],
        [6, 42],
        [13, 47],
        [46, 49],
        [14, 33],
        [41, 50],
        [19, 33],
        [24, 31],
        [47, 49],
        [32, 44],
        [23, 40],
        [31, 47],
        [11, 46],
        [17, 45],
        [10, 33],
        [17, 30],
        [43, 45],
        [49, 50],
        [13, 44],
        [16, 40],
        [44, 46],
        [1, 44],
        [6, 36],
        [39, 44],
        [21, 33],
        [3, 33],
        [33, 49],
        [32, 39],
        [4, 21],
        [9, 43],
        [33, 38],
        [32, 42],
        [31, 34],
        [16, 46],
        [27, 31],
        [8, 48],
        [2, 7],
        [25, 48],
        [4, 6],
        [22, 49],
        [38, 42],
        [19, 27],
        [10, 25],
        [32, 49],
        [5, 20],
        [1, 19],
        [21, 24],
        [32, 36],
        [22, 43],
        [3, 43],
        [9, 38],
        [41, 44],
        [25, 26],
        [37, 43],
        [28, 29],
        [24, 37],
        [36, 48],
        [27, 48],
        [26, 40],
        [21, 42],
        [11, 14],
        [44, 48],
        [16, 17],
        [40, 46],
        [2, 19],
        [41, 47],
        [22, 27],
        [13, 25],
        [36, 47],
        [24, 47],
        [37, 46],
        [9, 11],
        [41, 49],
        [19, 32],
        [43, 50],
        [8, 16],
        [47, 48],
        [27, 32],
        [48, 49],
        [22, 26],
        [34, 50],
        [32, 46],
        [21, 23],
        [35, 43],
        [17, 31],
        [35, 37],
        [12, 39],
        [24, 44],
        [35, 39],
        [18, 43],
        [8, 26],
        [38, 46],
        [43, 49],
        [20, 24],
        [8, 43],
        [40, 44],
        [30, 40],
        [24, 35],
        [6, 34],
        [2, 25],
        [23, 27],
        [11, 28],
        [15, 44],
        [46, 50],
        [5, 32],
        [25, 36],
        [37, 49],
        [1, 46],
        [21, 35],
        [20, 29],
        [45, 49],
        [8, 40],
        [30, 37],
        [1, 29],
        [22, 31],
        [13, 21],
        [36, 43],
        [2, 26],
        [4, 9],
        [18, 34],
        [37, 39],
        [34, 45],
        [14, 27],
        [6, 35],
        [15, 18],
        [39, 49],
        [7, 48],
        [39, 41],
        [32, 34],
        [40, 47],
        [14, 32],
        [10, 40],
        [9, 32],
        [13, 15],
        [41, 46],
        [13, 24],
        [36, 40],
        [16, 20],
        [19, 46],
        [2, 20],
        [41, 48],
        [14, 20],
        [19, 20],
        [15, 17],
        [22, 35],
        [5, 41],
        [32, 47],
        [6, 38],
        [4, 50],
        [33, 46],
        [36, 45],
        [1, 8],
        [42, 46],
        [24, 45],
        [40, 50],
        [12, 43],
        [8, 27],
        [19, 30],
    ]
    assert not solution(n, dislike)
