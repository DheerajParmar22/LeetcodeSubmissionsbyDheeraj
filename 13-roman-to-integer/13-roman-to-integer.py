class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            # 'IV': 4,
            'V': 5, 
            # 'IX': 9, 
            'X': 10,
            # 'XL': 40,
            'L': 50, 
            # 'XC': 90,
            'C': 100,
            # 'CD': 400,
            'D': 500,
            # 'CM': 900,
            'M': 1000
              }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC",                     "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: roman_to_integer[x], s))
        
        
        
        
        
        
        
#         sum = 0
#         i = 0
#         for i in s:
#             if s[i] == I:
#                 sum += 1
#             elif s[i] == V:
#                 sum += 5
#             elif s[i] == X:
#                 sum += 10
#             elif s[i] == L:
#                 sum += 50
#             elif s[i] == C:
#                 sum += 100
#             elif s[i] == D:
#                 sum += 500
#             else:
#                 sum += 1000
                
#         return sum
            
        