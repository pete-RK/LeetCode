from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m-1 # pointer for nums1
        j = n-1 # pointer for nums2
        k = m+n-1 # pointer for end of nums1

        # loop through the values of nums1[:m] & nums2[:n] from last to first
        while i >= 0 and j >= 0:
            # assign the greater value between nums1 & nums2 array for the current kth pointer
            if nums1[i] < nums2[j]:
                # assign nums2[j] value to nums1[k]
                nums1[k] = nums2[j]
                j -= 1
            #  do the inverse
            else:
                # assign nums1[i] value to nums1[k]
                nums1[k] = nums1[i]
                # move one value left
                i -= 1
            # move one value left
            k -= 1
        
        # copy left over values from nums2 to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1



        
        
