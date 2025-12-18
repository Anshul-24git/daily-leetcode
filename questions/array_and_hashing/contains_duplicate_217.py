class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) != len(nums)
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False
        
'''
nums = [1, 2, 3, 1]
i = 0
    num = 1, seen = {} -> add 1, seen = {1}
i = 1
    num = 2, seen = {1} -> add 2, seen = {1, 2}
i = 2
    seen = {1, 2, 3}
i = 3
    num = 1, seen = {1, 2, 3} -> 1 already exisits -> return True
Output - true

Time comp - O(n) - single pass
Space comp - O(n) - worst case, store every element
'''
