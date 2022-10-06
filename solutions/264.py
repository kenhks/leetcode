import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Iterative
    Time Complexity: O(nlog(10, n))
    Space Complexity: O(n)
    """

    def nthUglyNumber(self, n: int) -> int:
        def isUgly(n: int) -> bool:
            if n <= 0:
                return False
            for p in [2, 3, 5]:
                while n % p == 0:
                    n /= p
            return n == 1

        ugly_numbers = [1]
        next_num = 2
        while len(ugly_numbers) < n:
            if isUgly(next_num):
                ugly_numbers.append(next_num)
            next_num += 1
        print(f"{ugly_numbers = }")
        return ugly_numbers[-1]


class Solution2:
    """
    Generate in order
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        p2 = p3 = p5 = 0
        while len(ugly_numbers) < n:
            while ugly_numbers[p2] * 2 <= ugly_numbers[-1]:
                p2 += 1
            while ugly_numbers[p3] * 3 <= ugly_numbers[-1]:
                p3 += 1
            while ugly_numbers[p5] * 5 <= ugly_numbers[-1]:
                p5 += 1
            ugly_numbers.append(min(ugly_numbers[p2] * 2, ugly_numbers[p3] * 3, ugly_numbers[p5] * 5))
        return ugly_numbers[-1]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "nthUglyNumber",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(10) == 12


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(1) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(14) == 20


# @pytest.mark.parametrize("solution", solutions)
# def test_4(solution):
#     assert solution(100) == 1536
