class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(word: str):
            new_s = list(word)
            start, end = 0, len(word) - 1
            while start < end:
                new_s[start], new_s[end] = new_s[end], new_s[start]
                start += 1
                end -= 1
            return "".join(new_s)

        new_words = []
        last_word = 0
        for i, char in enumerate(s):
            if char == " ":
                new_words.append(reverse(s[last_word:i]))
                last_word = i + 1
        new_words.append(reverse(s[last_word : len(s)]))
        return " ".join(new_words)


class Solution2:
    def reverseWords(self, s: str) -> str:
        return " ".join(i[::-1] for i in s.split(" "))


def test_1():
    assert (
        Solution().reverseWords("Let's take LeetCode contest")
        == "s'teL ekat edoCteeL tsetnoc"
    )


def test_2():
    assert Solution().reverseWords("God Ding") == "doG gniD"


def test_3():
    assert (
        Solution2().reverseWords("Let's take LeetCode contest")
        == "s'teL ekat edoCteeL tsetnoc"
    )


def test_4():
    assert Solution2().reverseWords("God Ding") == "doG gniD"
