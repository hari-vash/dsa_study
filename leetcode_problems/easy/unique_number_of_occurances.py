class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        -----GIVEN EXAMPLE-----
        Input: arr = [1,2,2,1,1,3]
        Output: true
        -----------------------
        hashmap = {}
        for
            1 in arr
                1 not in hashmap:
                    hashmap[1] = 1                  => hashmap = {1:1}
            2 in arr
                2 not in hashmap:
                    hashmap[2] = 2                  => hashmap = {1:1,2:1}
            2 in arr
                2 in hashmap
                    hashmap[2] += 1                 => hashmap = {1:1,2:2}
            1 in arr
                1 in hashmap:
                    hashmap[1] += 1                 => hashmap = {1:2,2:2}
            1 in arr
                1 in hashmap
                    hashmap[1] += 1                 => hashmap = {1:3,2:2}
            3 in arr
                3 not in hashmap:
                    hashmap[3] = 1                  => hashmap = {1:3,2:2,3:1}
        sett = set(hashmap.values())                => sett = {3,2,1}
        
        return len(sett) == len(hashmap.values())   => return True              => solution
        """
        hashmap = {}
        for i in arr:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        sett = set(hashmap.values())

        return len(sett) == len(hashmap.values())