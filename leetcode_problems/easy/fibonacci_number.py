class Solution:
    def fib(self, n: int) -> int:
        """
        -----GIVEN EXAMPLE-----
        Input: n = 4
        Output: 3
        -----------------------
        n!=0
        n!=1
        
        prev = 0
        cur = 1
        
        for i = 2
            prev, cur = 1, 0+1 => prev, cur = 1,1
        
        for i = 3
            prev, cur = 1, 1+1 => prev, cur = 1,2
        
        for i = 4
            prev, cur = 2, 2+1 => prev, cur = 2,3
        
        return cur      => output = 3
        """
        if n==0:
            return 0
        if n==1:
            return 1
        
        prev = 0
        cur = 1
        for i in range(2,n+1):
            prev, cur = cur,prev+cur
        
        return cur