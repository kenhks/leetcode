import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Convertsion between str and int
    Time Complexity: O(m + n) = m + n + max(m, n) + log(2, max(m, n))
    Space Complexity: O(1)
    m = len(a), n = len(b)
    """

    def addBinary(self, a: str, b: str) -> str:
        return f"{int(a, 2) + int(b, 2):b}"


class Solution2:
    """
    Bitwise operation using str
    Time Complexity: O(max(m, n))
    Space Complexity: O(max(m, n))
    m = len(a), n = len(b)
    """

    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a
        result = []
        i, j = len(a) - 1, len(b) - 1

        def sum_str_binary(x, y, carry):
            if x == y:
                if not carry:
                    digit = "0"
                else:
                    digit = "1"
                if x == "1":
                    carry = 1
                else:
                    carry = 0
            else:
                if carry:
                    digit = "0"
                    carry = 1
                else:
                    digit = "1"
            return digit, carry

        carry = 0
        while i >= 0 and j >= 0:
            digit, carry = sum_str_binary(a[i], b[j], carry)
            result.append(digit)
            i -= 1
            j -= 1
        for i2 in range(i, -1, -1):
            digit, carry = sum_str_binary(a[i2], "0", carry)
            result.append(digit)
        if carry:
            result.append("1")
        return "".join(result[::-1])


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "addBinary",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(a="11", b="1") == "100"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(a="1010", b="1011") == "10101"
