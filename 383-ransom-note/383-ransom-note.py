class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections
        # note,mag = Counter(ransomNote), Counter(magazine)
        # if note & mag == note: return True
        # return False
        
        
        if Counter(ransomNote) & Counter(magazine) == Counter(ransomNote):
            return True
        else:
            return False
        
        