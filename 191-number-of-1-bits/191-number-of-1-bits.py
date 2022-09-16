class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # count = 0
        # n = str(n)
        # for i in range(len(n)):
        #     if n[i] == "1":
        #         count += 1
        #         # i++
        # return count("1")
        
        return bin(n).count("1")
                