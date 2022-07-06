class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        for x in range(len(nums1)):
            if i>=n:
                break
            if nums1[x]==0:
                nums1[x]=nums2[i]
                i+=1           
        nums1.sort()
        
        
        
        
#         last, i, j = m + n - 1, m - 1, n - 1

#         while i >= 0 and j >= 0:
#             if nums1[i] > nums2[j]:
#                 nums1[last] = nums1[i]
#                 last, i = last - 1, i - 1
#             else:
#                 nums1[last] = nums2[j]
#                 last, j = last - 1, j - 1

#         while j >= 0:
#                 nums1[last] = nums2[j]
#                 last, j = last - 1, j - 1
        
        
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        