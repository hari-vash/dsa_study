class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        -----GIVEN EXAMPLE-----
        Input: s = "anagram", t = "nagaram"
        Output: true
        -----------------------
        len(s) == len(t) => skips if block
        
        s_dic, t_dic = {},{}
        calling count_char function for both the dictionaries
        =>count_char(s_dic,s)
            for 
                char = a
                char not in my_dic
                my_dic['a']=1       => my_dic = {'a':1}
            for 
                char = n
                char no in my_dic
                my_dic['n'] = 1     => my_dic = {'a':1,'n':1}
            for 
                char = a
                char in my_dic
                my_dic['a'] += 1    => my_dic = {'a':2,'n':1}
            for 
                char = g
                char not in my_dic
                my_dic['g'] = 1     => my_dic = {'a':2,'n':1,'g':1}
            for 
                char = r
                char not in my_dic
                my_dic['r'] = 1     => my_dic = {'a':2,'n':1,'g':1,'r':1}
            for
                char = a
                char in my_dic
                my_dic['a'] += 1    => my_dic = {'a':3,'n':1,'g':1,'r':1}
            for
                char = m
                char not in my_dic
                my_dic['m'] = 1     => my_dic = {'a':3,'n':1,'g':1,'r':1,'m':1}
            return my_dic        
        => s_dic = {'a':3,'n':1,'g':1,'r':1,'m':1}, similarly t_dic = {'n':1,'a':3,'g':1,'r':1,'m':1}
        since, s_dic == t_dic
            RETURN TRUE
        """
        if len(s)!=len(t):
            return False
        
        def count_char(my_dic:dict, s:str):
            for char in s:
                if char in my_dic:
                    my_dic[char] += 1
                else:
                    my_dic[char] = 1
            return my_dic
            
        s_dic, t_dic = {}, {}
        s_dic, t_dic = count_char(s_dic,s), count_char(t_dic,t)

        if s_dic == t_dic:
            return True
        return False