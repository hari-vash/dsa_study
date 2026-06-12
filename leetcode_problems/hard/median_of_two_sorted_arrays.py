class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        -----GIVEN EXAMPLE-----
        Input: nums1 = [1,3], nums2 = [2]
        Output: 2.00000
        -----------------------
        nums3 = nums1 + nums2       => nums3 = [1,3,2]
        length = len(nums3)         => length = 3
        nums3.sort()                => nums3 = [1,2,3]
        
        lenght%2!=0
            return nums3[int(length/2)]     => nums3[1]     => return 2.0
        """
        nums3 = nums1 + nums2
        length = len(nums3)
        nums3.sort()

        if length%2==0:
            return (nums3[int(length/2)] + nums3[int(length/2)-1])/2
        else:
            return nums3[int(length/2)]