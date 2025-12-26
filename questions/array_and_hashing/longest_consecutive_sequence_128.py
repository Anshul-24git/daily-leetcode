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

        numSet = set(nums)
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

        Brute force:
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


        '''
