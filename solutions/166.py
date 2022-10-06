import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Use hashmap to check recurring remainder
    Time Complexity: O(k)
    Space Complexity: O(k)
    k = size of unique remainder
    """

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = ""
        if (numerator < 0) ^ (denominator < 0) and numerator != 0:
            sign = "-"
        remainders_map = {}
        denominator = abs(denominator)
        integer_part, remainder = divmod(abs(numerator), denominator)
        decimal_part = "."
        while remainder != 0:
            if remainder in remainders_map:
                decimal_part = f"{decimal_part[:remainders_map[remainder]]}({decimal_part[remainders_map[remainder]:]})"
                break
            remainders_map[remainder] = len(decimal_part)
            digit, remainder = divmod(remainder * 10, denominator)
            decimal_part += f"{digit}"
        if len(decimal_part) == 1:
            decimal_part = ""
        return f"{sign}{integer_part}{decimal_part}"


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "fractionToDecimal",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(1, 2) == "0.5"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(2, 1) == "2"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(4, 333) == "0.(012)"
