class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""
        for i, j in zip(word1, word2):
            merged_word += i + j
        if len(word2) > len(word1):
            merged_word += word2[len(word1) - len(word2) :]
        elif len(word1) > len(word2):
            merged_word += word1[len(word2) - len(word1) :]
        return merged_word


def test_1():
    assert Solution().mergeAlternately("abc", "pqr") == "apbqcr"


def test_2():
    assert Solution().mergeAlternately("ab", "pqrs") == "apbqrs"


def test_3():
    assert Solution().mergeAlternately("abcd", "pq") == "apbqcd"
