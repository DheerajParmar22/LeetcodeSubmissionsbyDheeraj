class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp={'a':1,'e':1,'i':1,'o':1,'u':1}
        
        for i in range(n-1):
            dp1={}
            for c in 'aeiou':
                if c=='a':
                    dp1[c]=dp['e']
                elif c=='e':
                    dp1[c]=dp['a']+dp['i']
                elif c=="i":
                    dp1[c]=dp['a']+dp['e']+dp['o']+dp['u']
                elif c=='o':
                    dp1[c]=dp['i']+dp['u']
                elif c=='u':
                    dp1[c]=dp['a']
                    
            dp=dp1
        mod=10**9+7    
        return sum(dp.values())%mod