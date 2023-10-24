class Solution(object):
    def strStr(self, haystack, needle):
        haystack_len = len(haystack)

        for i, _ in enumerate(haystack):
            if haystack[i] == needle[0]:
                if haystack_len >= len(needle):
                    for j, _ in enumerate(needle):
                        if haystack[i + j] != needle[j]:
                            break
                        if len(needle) == j + 1:
                            return i
            haystack_len -= 1
        return -1

    