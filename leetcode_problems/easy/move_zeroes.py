class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        -----GIVEN EXAMPLE-----
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]
        -----------------------
        left = 0
        
        for right in range(5):
            right = 0
                if nums[0]!=0:                                          => false
            right = 1
                if nums[1]!=0:                                          => true
                    nums[left],nums[right] = nums[right],nums[left]     => nums[0],nums[1] = 1,0       => nums = [1,0,0,3,12]
                    left += 1                                           => left = 1
            right = 2
                if nums[2]!=0:                                          => false
            right = 3
                if nums[3]!=0:                                          => true
                    nums[left],nums[right] = nums[right],nums[left]     => nums[1],nums[3] = 3,0       => nums = [1,3,0,0,12]
                    left += 1                                           => left = 2
            right = 4
                if nums[4]!=0:                                          => true
                    nums[left],nums[right] = nums[right],nums[left]     => nums[2],nums[4] = 12,0       => nums = [1,3,12,0,0]      => solution
                    left += 1                                           => left = 3
        """ 
        left = 0

        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1