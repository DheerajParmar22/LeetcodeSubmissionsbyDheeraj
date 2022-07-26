class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        number = ''
        for i in digits:
            number += str(i)
        number = str(int(number) + 1)
        result = [x for x in number]
        return result
            
            
        