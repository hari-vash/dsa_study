class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        -----GIVEN EXAMPLE-----
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        -----------------------
        count_frequent_elements = {}
        solution = []
        
        for i=1
            i not in count_frequent_elements
                count_frequent_elements[i] = 1      => count_frequent_elements = {1:1}
        
        for i=1
            i in count_frequent_elements
                count_frequent_elements[i] += 1     => count_frequent_elements = {1:2}
                
        for i=1
            i in count_frequent_elements
                count_frequent_elements[i] += 1     => count_frequent_elements = {1:3}
        
        for i=2
            i not in count_frequent_elements
                count_frequent_elements[i] = 1      => count_frequent_elements = {1:3,2:1}
            
        for i=2
            i in count_frequent_elements
                count_frequent_elements[i] += 1     => count_frequent_elements = {1:3,2:2}

        for i=3
            i not in count_frequent_elements
                count_frequent_elements[i] = 1      => count_frequent_elements = {1:3,2:2,3:1}

        sorted_fearray = sorted(
            count_frequent_elements,                => dictionary keys to sort
            key=count_frequent_elements.get,        => sort keys by their associated dictionary values
            reverse=True                            => descending order (largest value first)
        )
        
        => sorted_fearray = [1,2,3]
        
        solution.extend(sorted_fearray[:k])         => solution = [1,2]
        
        return solution
        """
        count_frequent_elements = {}
        solution = []

        for i in nums:
            if i in count_frequent_elements:
                count_frequent_elements[i] += 1
            else:
                count_frequent_elements[i] = 1

        sorted_fearray = sorted(count_frequent_elements,key=count_frequent_elements.get,reverse=True)
        
        solution.extend(sorted_fearray[:k])
        
        return solution