from collections import Counter

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^2) = n * (n - 1)
    Space Complexity: O(n)
    """

    def equalFrequency(self, word: str) -> bool:
        ans = False
        for i in range(len(word)):
            if len(set(Counter(word[:i] + word[i + 1 :]).values())) == 1:
                ans = True
                break
        return ans


class Solution2:
    """
    Hashmap Counter for word and word frequency
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def equalFrequency(self, word: str) -> bool:
        char_counter = Counter(word)
        ans = False
        if len(char_counter) == 1:
            ans = True
        else:
            freq_counter = Counter(char_counter.values())
            if len(freq_counter) == 2:
                freq1, freq2 = sorted(freq_counter.keys())
                print(f"{freq1, freq_counter[freq1] = }")
                print(f"{freq2, freq_counter[freq2] = }")
                if freq1 == 1 and freq_counter[freq1] == 1:
                    ans = True
                elif freq2 - freq1 == 1 and freq_counter[freq2] == 1:
                    ans = True
            elif len(freq_counter) == 1:
                freq = next(i for i in freq_counter)
                ans = freq == 1
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "equalFrequency",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("abcc")


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution("aazz")


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("abc")


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution("ddaccb")


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution("xy")


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert not solution("cbccca")


@pytest.mark.parametrize("solution", solutions)
def test_7(solution):
    assert solution("aca")


@pytest.mark.parametrize("solution", solutions)
def test_8(solution):
    assert solution("zz")


@pytest.mark.parametrize("solution", solutions)
def test_9(solution):
    assert solution("cccd")


@pytest.mark.parametrize("solution", solutions)
def test_10(solution):
    assert not solution("aaaabbbbccc")
