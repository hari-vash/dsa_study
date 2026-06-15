class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        -----GIVEN EXAMPLE-----
        Input: candies = [2,3,5,1,3], extraCandies = 3
        Output: [true,true,true,false,true] 
        -----------------------
        max_candies = max(candies)          => max_candies = 5
        
        [2 + 3 >= 5 for 2 in candies]       => [true]
        [3 + 3 >= 5 for 3 in candies]       => [true, true]
        [5 + 3 >= 5 for 5 in candies]       => [true, true, true]
        [1 + 3 >= 5 for 1 in candies]       => [true, true, true, false]
        [3 + 3 >= 5 for 3 in candies]       => [true, true, true, false, true]
        
        return [true, true, true, false, true]
        """
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]