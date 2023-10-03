class Solution:
    def isValid(self, s: str) -> bool:
        opening_symbols_stack = []
        symbols_correlation_map = {
            ')': '(', 
            ']': '[', 
            '}': '{'
        }
        
        for char in s:
            if char not in symbols_correlation_map:
                opening_symbols_stack.append(char)
            else:
                no_opening_symbol = len(opening_symbols_stack) == 0
                if no_opening_symbol:
                    return False
                
                opening_symbol = symbols_correlation_map[char]
                previous_symbol = opening_symbols_stack.pop()

                if opening_symbol != previous_symbol:
                    return False
        
        return len(opening_symbols_stack) == 0
    
