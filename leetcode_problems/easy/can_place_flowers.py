class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        -----GIVEN EXAMPLE-----
        Input: flowerbed = [1,0,0,0,1], n = 1
        Output: true
        -----------------------
        for i=0
            if flowerbed[0] != 0
            
        for i=1
            if flowerbed[1] == 0
                empty_left = False
        
        for i=2
            if flowerbed[2] == 0
                empty_left = True
                empty_right = True
            
                if empty_left and empty_right:
                    flowerbed[2] = 1                => flowerbed = [1,0,1,0,1]
                    count += 1                      => count = 1
            if count>=n                             => 1 >= 1
                return True                         => solution
        """
        count = 0
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
                    
            if count >= n:
                return True
                
        return count >= n