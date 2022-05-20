class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i, c in enumerate(s):
            if c in freq:
                freq[c].append(i)
            else:
                freq[c] = [i]
        return next((freq[i][0] for i in freq if len(freq[i]) == 1), -1)


def test_1():
    assert Solution().firstUniqChar("leetcode") == 0


def test_2():
    assert Solution().firstUniqChar("loveleetcode") == 2


def test_3():
    assert Solution().firstUniqChar("aabb") == -1
