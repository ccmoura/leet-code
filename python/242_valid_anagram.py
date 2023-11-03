class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        characteres = {}

        for char in s:
            if char in characteres:
                characteres[char] += 1
            else:
                characteres[char] = 1
        
        for char in t:
            if char not in characteres or characteres[char] == 0:
                return False
            else:
                characteres[char] -= 1

        return True
    