class Solution:
    def reverseWords(self, s: str) -> str:
        """
        -----GIVEN EXAMPLE-----
        Input: s = "  hello world  "
        Output: "world hello"
        -----------------------
        " ".join(s.split()[::-1])
        split original string into list(spaces are removed), reverse it, join with a string, return it
        
        s.split()                       => ["hello","world"]
        s.split()[::-1]                 => ["world","hello"]
        " ".join(s.split()[::-1])       => "world hello"
        return " "(s.split()[::-1])     => return "world hello"         => solution
        """
        return " ".join(s.split()[::-1])