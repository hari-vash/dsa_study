class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        -----GIVEN EXAMPLE-----
        nums = [3,2,4]
        target = 6
        -----------------------
        dictionary = {}
        for 
            i = 0, n = 3
            diff = 6 - 3 = 3
            diff not in dictionary
        dictionary = {3:0}
        
        for
            i = 1, n = 2
            diff = 6 - 2 = 4
            diff not in dictionary
        dictionary = {3:0, 2:1}
        
        for
            i = 2, n = 4
            diff = 6 - 4 = 2
            diff in dictionary
            return [dictionary[2],i] ===> [1,2] ====> SOLUTION
        ------------------------
        SOLUTION = [1,2]
        """
        dictionary = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in dictionary:
                return [dictionary[diff],i]
            dictionary[n]=i
        return