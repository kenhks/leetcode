import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Recursive
    Time Complexity: O(n) = n / ( 1 - 1 / k)
    Space Complexity: O(log(k, n))
    """

    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        return self.digitSum("".join([str(sum(int(j) for j in s[i : i + k])) for i in range(0, len(s), k)]), k)


class Solution2:
    """
    Iterative
    Time Complexity: O(n) = n / ( 1 - 1 / k)
    Space Complexity: O(log(k, n))
    """

    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = "".join([str(sum(int(j) for j in s[i : i + k])) for i in range(0, len(s), k)])
        return s


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "digitSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(s="11111222223", k=3) == "135"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(s="00000000", k=3) == "000"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(s="123", k=5) == "123"
