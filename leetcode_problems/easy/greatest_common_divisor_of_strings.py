class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        -----GIVEN EXAMPLE-----
        Input: str1 = "ABCABC", str2 = "ABC"
        Output: "ABC"
        -----------------------
        len1, len2 = len(str1),len(str2)                            => len1 = 6, len2 = 3
        
        for length in range(min(len1,len2),0,-1):                   => min(len1,len2) = 3

            if isDivisor(3):
            
            ---enters function---
            isDivisor(3)
                len1 % 3 == 0 or len2 % 3 == 0                     => skips if block
                
                factor1, factor2 = len1 // 3, len2 // 3             => factor1 = 2, factor2 = 1
                
                return str1[:3]*2 == str1 and str1[:3]*1 == str2    => return "ABC" * 2 == "ABCABC" and "ABC" * 1 == ABC    => return True
            ---exits function---
            
                return str1[:3]                                     => return "ABC"     => solution
        """
        len1, len2 = len(str1),len(str2)

        def isDivisor(length):
            if len1 % length != 0 or len2 % length != 0:
                return False
            factor1, factor2 = len1 // length, len2 // length
            return str1[:length]*factor1 == str1 and str1[:length]*factor2 == str2

        for length in range(min(len1,len2),0,-1):
            if isDivisor(length):
                return str1[:length]
        
        return ""