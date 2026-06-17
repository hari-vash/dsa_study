class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        -----GIVEN EXAMPLE-----
        Input: s = "IceCreAm"
        Output: "AceCreIm"
        -----------------------
        head = 0
        tail = len(s)-1                                                         => tail = 7
        letter = list(s)                                                        => letter = ['I', 'c', 'e', 'C', 'r', 'e', 'A', 'm']
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        while 
            7>0
                if letter[0] in vowels and letter[7] not in vowels              => skip if block
                elif letter[0] in vowels
                    tail -= 1                                                   => tail = 6
            6>0
                if letter[0] in vowels and letter[6] in vowels 
                    letter[head],letter[tail] = letter[tail], letter[head]      => letter = ['A', 'c', 'e', 'C', 'r', 'e', 'I', 'm']
                    head += 1                                                   => head = 1
                    tail -= 1                                                   => tail = 5
            5>1
                if letter[1] not in vowels and letter[5] in vowels              => skip if block
                elif letter[1] not in vowels                                    => skip elif block
                elif letter[5] in vowels
                    head += 1                                                   => head = 2
            5>2
                if letter[2] in vowels and letter[5] in vowels 
                    letter[head],letter[tail] = letter[tail], letter[head]      => letter = ['A', 'c', 'e', 'C', 'r', 'e', 'I', 'm']
                    head += 1                                                   => head = 3
                    tail -= 1                                                   => tail = 4
            4>3
                if letter[3] not in vowels and letter[4] in vowels              => skip if block
                elif letter[3] not in vowels                                    => skip elif block
                elif letter[4] not in vowels                                    => skip elif block
                else
                    head += 1                                                   => head = 4
                    tail -= 1                                                   => tail = 3
            3<4
                break
        
        return "".join(letter)                                                  =? return "AceCreIm"        => solution
        
        """
        head = 0
        tail = len(s)-1
        letter = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while tail > head:
            if letter[head] in vowels and letter[tail] in vowels:
                letter[head],letter[tail] = letter[tail],letter[head]
                head += 1
                tail -= 1
            elif letter[head] in vowels:
                tail -= 1
            elif letter[tail] in vowels:
                head += 1
            else:
                head += 1
                tail -= 1

        return "".join(letter)