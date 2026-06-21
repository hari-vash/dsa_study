class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        -----GIVEN EXAMPLE-----
        Input: s = "abc", t = "ahbgdc"
        Output: true
        -----------------------
        pointer1 = 0
        
        if not s:       => false
        
        for i in range(len(t)):             => len(t) = 6
            
            i = 0
            if pointer1 < len(s) and t[0] == s[0]:      => true and true
                pointer += 1                            => pointer1 = 1
            if pointer1 == len(s)                       => false
            
            i = 1
            if pointer1 < len(s) and t[1] == s[1]       => true and false
            if pointer1 == len(s)                       => false
            
            i = 2
            if pointer1 < len(s) and t[2] == s[1]:      => true and true
                pointer += 1                            => pointer1 = 2
            if pointer1 == len(s)                       => false
            
            i = 3
            if pointer1 < len(s) and t[3] == s[2]       => true and false
            if pointer1 == len(s)                       => false
            
            i = 4
            if pointer1 < len(s) and t[4] == s[2]       => true and false
            if pointer1 == len(s)                       => false
            
            i = 5
            if pointer1 < len(s) and t[5] == s[2]:      => true and true
                pointer += 1                            => pointer1 = 3
            if pointer1 == len(s)                       => true
                return True                             => Solution
        """
        pointer1 = 0

        if not s:
            return True

        for i in range(len(t)):
            if pointer1 < len(s) and t[i] == s[pointer1]:
                pointer1 += 1
            if pointer1 == len(s):
                return True
        
        return pointer1 == len(s)