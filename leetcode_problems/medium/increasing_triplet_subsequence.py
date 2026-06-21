class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        -----GIVEN EXAMPLE-----
        Input: nums = [1,2,3,4,5]
        Output: true
        -----------------------
        first = infinity
        second = infinity
        
        for i in nums:
            i = 1
                if 1 <= infinity:       => true
                    first = 1
            i = 2
                if 2 <= 1:              => false
                elif 2 <= infinity:     => true
                    second = 2
            i = 3
                if 3 <= 1:              => false
                elif 3 <= 2:            => false
                else:
                    return True         => solution (a consecutive element greater than first and second(first<second) found in the nums array)
        """
        first = float('inf')
        second = float('inf')

        for i in nums:
            if i<=first:
                first = i
            elif i<=second:
                second = i
            else:
                return True
            
        return False