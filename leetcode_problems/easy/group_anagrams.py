class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        -----GIVEN EXAMPLE-----
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        -----------------------
        anagram_groups ={}
        
        for
            s = eat
                signature = aet
                signature not in anagram_groups
                    anagram_groups["aet"] = []      => anagram_groups = {"aet":[]}
                anagram_groups["aet"].append(s)     => anagram_groups = {"aet":["eat"]}
        
        for
            s = tea
            signature = aet
            signature in anagram_groups             => skip if block
            anagram_groups["aet"].append(s)         => anagram_groupd = {"aet":["eat","tea"]}
            
        for
            s = tan
                signature = ant
                signature not in anagram_groups
                    anagram_groups["ant"] = []      => anagram_groups = {"aet":["eat","tea"],"ant":[]}
                anagram_groups["ant"].append(s)     => anagram_groups = {"aet":["eat","tea"],"ant":["tan"]}
            
        for
            s = ate
                signature = aet
                signature in anagram_groups         => skip if block
                anagram_groups["aet"].append(s)     => anagram_groups = {"aet":["eat","tea","ate"],"ant":["tan"]}
                
        for
            s = nat
                signature = ant
                signature in anagram_groups         => skip if block
                anagram_groups["ant"].append(s)     => anagram_groups = {"aet":["eat","tea","ate"],"ant":["tan","nat"]}
        
        for
            s = bat
                signature = abt
                signature not in anagram_groups
                    anagram_groups["abt"] = []      => anagram_groups = {"aet":["eat","tea","ate"],"ant":["tan","nat"],"bat":[]}
                anagram_groups["abt"].append(s)     => anagram_groups = {"aet":["eat","tea","ate"],"ant":["tan","nat"],"abt":[bat]}
        
        return list(anagram_groups.values())        => [["eat","tea","ate"],["tan","nat"],[bat]]        => solution (any order)
        """
        anagram_groups = {}

        for s in strs:
            signature = "".join(sorted(s)) 
            if signature not in anagram_groups:
                anagram_groups[signature] = []
            anagram_groups[signature].append(s)
        
        return list(anagram_groups.values())