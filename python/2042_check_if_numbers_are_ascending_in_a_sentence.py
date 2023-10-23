class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split()
        last_number = -1

        for token in tokens:
            if token.isdigit():
                number = int(token)
                if number <= last_number:
                    return False
                last_number = number
        return True
