class Solution(object):
    def compute_lps_array(self, needle):
        needle_len = len(needle)
        lps = [0] * needle_len
        i = 1
        length = 0

        while i < needle_len:
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def strStr(self, haystack, needle):
        haystack_len = len(haystack)
        needle_len = len(needle)
        lps = self.compute_lps_array(needle)

        i = 0
        j = 0

        while (haystack_len - i) >= (needle_len - j):
            if needle[j] == haystack[i]:
                j += 1
                i += 1
            
            if j == needle_len:
                return i - j
            elif i < haystack_len and needle[j] != haystack[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

