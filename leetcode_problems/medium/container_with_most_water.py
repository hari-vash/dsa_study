class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        -----GIVEN EXAMPLE-----
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        -----------------------
        left = 0
        right = len(height) - 1                 => right = 8
        maxArea = 0
        
        while left<right:
            while 0<8:                                                                  => true
                currentArea = min(height[left],height[right]) * (right - left)          => currentArea = min(1,7)*(8-0)     => currentArea = 8
                maxArea = max(maxArea,currentArea)                                      => maxArea = max(0,8)               => maxArea = 8
                
                if height[left]<height[right]:                                          => true
                    left += 1                                                           => left = 1
                
            while 1<8:                                                                  => true
                currentArea = min(height[left],height[right]) * (right - left)          => currentArea = min(8,7)*(8-1)     => currentArea = 49
                maxArea = max(maxArea,currentArea)                                      => maxArea = max(8,49)              => maxArea = 49
                
                if height[left]<height[right]:                                          => false
                    right -= 1                                                          => right = 7
            
            while 1<7:                                                                  => true
                currentArea = min(height[left],height[right]) * (right - left)          => currentArea = min(8,3)*(7-1)     => currentArea = 18
                maxArea = max(maxArea,currentArea)                                      => maxArea = max(49,18)             => maxArea = 49
                
                if height[left]<height[right]:                                          => false
                    right -= 1                                                          => right = 6
                    
            while 1<6:                                                                  => true
                currentArea = min(height[left],height[right]) * (right - left)          => currentArea = min(8,8)*(6-1)     => currentArea = 40
                maxArea = max(maxArea,currentArea)                                      => maxArea = max(49,40)             => maxArea = 49
                
                if height[left]<height[right]:                                          => false
                    right -= 1                                                          => right = 5
                    
            while 1<5:                                                                  => true
                currentArea = min(height[left],height[right]) * (right - left)          => currentArea = min(8,4)*(5-1)     => currentArea = 16
                maxArea = max(maxArea,currentArea)                                      => maxArea = max(49,16)             => maxArea = 49
                
                if height[left]<height[right]:                                          => false
                    right -= 1                                                          => right = 4
                    
            while 1<4:                                                                  => true
                currentArea = min(height[left],height[right]) * (right - left)          => currentArea = min(8,5)*(4-1)     => currentArea = 15
                maxArea = max(maxArea,currentArea)                                      => maxArea = max(49,15)             => maxArea = 49
                
                if height[left]<height[right]:                                          => false
                    right -= 1                                                          => right = 3
                    
            while 1<3:                                                                  => true
                currentArea = min(height[left],height[right]) * (right - left)          => currentArea = min(8,2)*(3-1)     => currentArea = 4
                maxArea = max(maxArea,currentArea)                                      => maxArea = max(49,4)              => maxArea = 49
                
                if height[left]<height[right]:                                          => false
                    right -= 1                                                          => right = 2

            while 1<2:                                                                  => true
                currentArea = min(height[left],height[right]) * (right - left)          => currentArea = min(8,6)*(2-1)     => currentArea = 6
                maxArea = max(maxArea,currentArea)                                      => maxArea = max(49,6)              => maxArea = 49
                
                if height[left]<height[right]:                                          => false
                    right -= 1                                                          => right = 1

            while 1<1:                                                                  => false
        
        return maxArea                                                                  => return 49                        => solution
        """
        left = 0
        right = len(height)-1
        maxArea = 0

        while left < right:
            currentArea = min(height[left],height[right]) * (right - left)
            maxArea = max(maxArea,currentArea)

            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea