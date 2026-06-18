class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        -----GIVEN EXAMPLE-----
        Input: nums1 = [1,2,3], nums2 = [2,4,6]
        Output: [[1,3],[4,6]]
        -----------------------
        set1, set2 = set(nums1),set(nums2)                          => set1 = {1,2,3} , set2 = {2,4,6}
        
        return [list(set1 - set2),list(set2 - set1)]                => return [elements in set1 but not in set2, elements in set2 but not in set1]
                [list({1,2,3} - {2,4,6}), list({2,4,6} - {1,2,3})]
                [list({1,3}),list({4,6})]

        return [[1,3],[4,6]]                                        => solution
        """
        set1, set2 = set(nums1),set(nums2)
        return [list(set1 - set2),list(set2 - set1)]