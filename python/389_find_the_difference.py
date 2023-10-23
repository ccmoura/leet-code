class Solution(object):
    def findTheDifference(self, s, t):
        s_letters_occurrences = {}

        for i in s:
            if s_letters_occurrences.get(i) != None:
                s_letters_occurrences[i] += 1
            else:
                s_letters_occurrences[i] = 1
        
        for i in t:
            occurrence = s_letters_occurrences.get(i)
            if occurrence == None or occurrence == 0:
                return i
            else:
                s_letters_occurrences[i] -= 1
