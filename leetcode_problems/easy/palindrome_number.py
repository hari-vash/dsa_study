class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        -----GIVEN EXAMPLE-----
        x = 121
        -----------------------
        skips first two if blocks
        
        num = 0
        num_original = 121
        
        while 121!=0
            num = 0 * 10 + (121%10) = 0 + 1
            x = 121//10 = 12
            
        while 12!=0
            num = 1 * 10 + (12%10) = 10 + 2 = 12
            x = 12//10 = 1
            
        while 1!=0
            num = 12*10 + (1%10) = 120 + 1 = 121
            x = 1//10 = 0

            BREAK
        
        num == num_original => 121 == 121
        returns True
        """
        if (x>=0 and x<=9):
            return True
        if (x%10==0 or x<0):
            return False
        num = 0
        num_original = x
     
        while x!=0:
            num = num*10 + (x%10)
            x = x//10
        if num == num_original:
            return True
        else:
            return False