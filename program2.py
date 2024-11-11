from itertools import pairwise
class Solution(object):
    def romanToInt(self, s):
         if not s:
            return 0
        
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Sum the value of each character and handle subtraction rule based on the pairwise comparison
        return sum((-1 if d[a] < d[b] else 1) * d[a] for a, b in pairwise(s)) + d[s[-1]]
        pass



