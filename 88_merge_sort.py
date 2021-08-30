from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2
        else:
            i = m - 1       # pointer to nums1
            j = n - 1       # pointer to nums2
            t = m + n - 1   # pointer to final list nums2

            while(j >= 0):
                if(i >= 0 and nums1[i] > nums2[j]):
                    nums1[t] = nums1[i]
                    t -= 1
                    i -= 1
                else:
                    nums1[t] = nums2[j]
                    t -= 1
                    j -= 1
                        

test1 = Solution()
test1.merge([1,2,3,0,0,0], 3, [2,4,6], 3)
  