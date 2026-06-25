class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        -----GIVEN EXAMPLE-----
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        -----------------------
        n = len(nums)                       => n = 4
        result = [1]*n                      => result = [1,1,1,1]
        
        left_product = 1
        for i in range(n):
            i = 0
                result[i] = left_product        => result[0] = 1        => result = [1,1,1,1]
                left_product *= nums[i]         => left_product = 1
            i = 1
                result[i] = left_product        => result[1] = 1        => result = [1,1,1,1]
                left_product *= nums[i]         => left_product = 2
            i = 2
                result[i] = left_product        => result[2] = 2        => result = [1,1,2,1]
                left_product *= nums[i]         => left_product = 6
            i = 3
                result[i] = left_product        => result[3] = 6        => result = [1,1,2,6]
                left_product *= nums[i]         => left_product = 24
        
        right_product = 1
        for i in range(n-1,-1,-1):
            i = 3
                result[i] *= right_product      => result[3] = 6*1 = 6              => result = [1,1,2,6]
                right_product *= nums[i]        => right_product = 4
            i = 2
                result[i] *= right_product      => result[2] = 2*4 = 8              => result = [1,1,8,6]
                right_product *= nums[i]        => right_product = 12
            i = 1
                result[i] *= right_product      => result[1] = 1*12 = 12            => result = [1,12,8,6]
                right_product *= nums[i]        => right_product = 24
            i = 0
                result[i] *= right_product      => result[0] = 1*24 = 24            => result = [24,12,8,6]
                right_product *= nums[i]        => right_product = 24

        return result                           => result = [24,12,8,6]             => solution
        """
        n = len(nums)
        result = [1] * n

        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
            
        return result
