class Solution(object):
    def mergeAlternately(self, word1, word2):
        word1_len = len(word1)
        word2_len = len(word2)
        shortest_string_len = word1_len if word1_len < word2_len else word2_len
        merged = ""

        for i in range(shortest_string_len):
            merged += word1[i] + word2[i]

        merged += word1[shortest_string_len:] if word1_len > word2_len else word2[shortest_string_len:]
        return merged
