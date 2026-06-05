class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        -----GIVEN EXAMPLE-----
        Input: nums = [1,2,3,1]
        Output: true
        -----------------------
        sett = set()
        for
            1 not in sett
            sett.add(1)     => sett = {1}
        for 
            2 not in sett
            sett.add(2)     => sett = {1,2}
        for
            3 not in sett
            sett.add(3)     => sett = {1,2,3}
        for
            1 in sett
                RETURN TRUE
        """
        sett = set()
        for i in nums:
            if i in sett:
                return True
            sett.add(i)
        return False