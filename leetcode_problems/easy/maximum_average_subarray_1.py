class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        -----GIVEN EXAMPLE-----
        Input: nums = [1,12,-5,-6,50,3], k = 4
        Output: 12.75000
        -----------------------
        n = len(nums)       => n = 6
        cur_sum = 0
        for i in range(4):
            i = 0
                cur_sum += nums[i]          => cur_sum = 1
            similarly for i=1,2,3           => cur_sum = 2
        max_average = 2/4                   => max_average = 0.5
        
        for i in range(k,n):
            i = 4
            cur_sum += nums[i]              => cur_sum = 52
            cur_sum -= nums[i-k]            => cur_sum = 51
            average = 51 / 4                => average = 12.75
            max_average = max(0.5,12.75)    => max_average = 12.75
            
            i = 5
            cur_sum += nums[i]              => cur_sum = 54
            cur_sum -= nums[i-k]            => cur_sum = 42
            average = 42 / 4                => average = 10.5
            max_average = max(12.75,10.5)    => max_average = 12.75
        
        return max_average                  => return 12.75         => solution
        """
        n = len(nums)
        cur_sum = 0

        for i in range(k):
            cur_sum += nums[i]
        max_average = cur_sum / k
        
        for i in range(k,n):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            
            average = cur_sum / k
            max_average = max(max_average,average)
            
        return max_average