#User function Template for python3

class Solution:
	def brainGame(self, nums):
	    ans = [0]*1001
		for i in range(2,1001):
		    for j in range(2*i,1001,i):
		        ans[j] = max(ans[j],1+ans[i])
		res = 0
        for i in range(len(nums)):
            res = res^ans[nums[i]]
        if res==0:
            return False
        return True
		# Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int,input().split()))
		ob = Solution()
		ans = ob.brainGame(nums)
		if(ans):
			print("A")
		else:
			print("B")

# } Driver Code Ends