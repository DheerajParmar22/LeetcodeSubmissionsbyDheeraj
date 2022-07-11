class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import collections
        
        if Counter(s) == Counter(t):
            return True
        else:
            return False