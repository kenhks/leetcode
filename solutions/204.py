import math

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Find the odd number which can not be factorize as prime
    Time Complexity: O(n^2) = Summation{3, i=n, 2}{i ^ (3/2)}
    Space Complexity: O(n)
    """

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [2]
        for i in range(3, n, 2):
            i_sqrt = math.floor(math.sqrt(i))
            is_prime = True
            for p in primes[1:]:
                if p > i_sqrt:
                    break
                if i % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
        return len(primes)


class Solution2:
    """
    Sieve of Eratosthenes
    Time Complexity: O(n * log(2, log(2, n)))
    Space Complexity: O(n)
    """

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        nums = [1] * n
        nums[0] = 0
        nums[1] = 0
        for i in range(2, math.ceil(math.sqrt(n))):
            if nums[i]:
                nums[i * i : n : i] = [0] * ((n - 1 - i * i) // i + 1)
        return sum(nums)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "countPrimes",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(10) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(0) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(1) == 0


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(2) == 0


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(100) == 25


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert solution(3) == 1


@pytest.mark.parametrize("solution", solutions)
def test_7(solution):
    assert solution(499979) == 41537
