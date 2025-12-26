class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # num_set = set(nums)
        # max_length = 0

        # for num in num_set:
        #     if (num - 1) not in num_set:
        #         current_num = num
        #         current_length = 1
        #         while current_num + 1 in num_set:
        #             current_num += 1
        #             current_length += 1
        #         max_length = max(max_length, current_length)
        # return max_length

        numSet = set(nums) #converting to set for faster lookups
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest        
        '''
        nums = [100, 4, 200, 1, 3, 2]
        o/p : 4

        Brute force (this) :
            counter() = 0
            sort(nums)
            0 to (n-1)
            for num in nums:
                if num + 1 exists:
                    count ++
                    num++
            return count
        
        Optimized solution (HashSet) :
            (num - 1)

        nums = [100, 4, 200, 1, 3, 2]
        num_set = {100, 4, 200, 1, 3, 2}

        process 100 : num - 1 (check for 99) -> not there
            num = 100
            current_length = 1
            check num + 1 (101) in set
            not found
        process 4 : num - 1 (check for 3) - found it
            skip
        process 200 : same as 100
        process 1 : num - 1 (check for 0) -> not there
            this is the start
            sequence : 1 - 2 - 3 - 4
            length : 4
        check for the rest of the nums as well
        '''
