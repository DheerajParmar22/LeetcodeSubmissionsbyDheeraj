class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        queue = list(range(n,0,-1))
        curr_k =  k-1
        while len(queue) != 1:
            while curr_k != 0:
                queue.insert(0,queue.pop())
                curr_k -= 1
            
            queue.pop()
            curr_k = k-1
            
        return queue.pop()
        