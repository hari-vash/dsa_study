class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        -----GIVEN EXAMPLE-----
        Input: word1 = "ab", word2 = "pqrs"
        Output: "apbqrs"
        -----------------------
        word3 = ""
        
        len(word1)<len(word2)
            length, word = len(word1), word2        => length = 2, word = "pqrs"
        
        while i < length
            i = 0
                word3 += word1[i]                         => word3 = "a"
                word3 += word2[i]                         => word3 = "ap"
                i += 1                                    => i = 1
            i = 1
                word3 += word1[i]                         => word3 = "apb"
                word3 += word2[i]                         => word3 = "apbq"
                i += 1                                    => i = 2
            break
        word3 += word[i:]                                 => word3 += word[2:]      => word3 = "apbqrs" 
        
        return word3                                      => solution
        """
        word3 = ""
        if len(word1)<len(word2):
            length, word = len(word1),word2
        else:
            length, word = len(word2),word1
        i = 0
        while i < length:
            word3+=word1[i]
            word3+=word2[i]
            i+=1
        word3+=word[i:]
        return word3