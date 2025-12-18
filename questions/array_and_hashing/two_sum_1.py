class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in visited:
                return [visited[comp], i]

            visited[num] = i

        return False
        
        '''
        nums = [2,7,11,15] , target = 9

        i = 0, num = 2, complement -> 9 - 2 = 7 -> {2:0}
        i = 1, num = 7, complement -> 9 - 7 = 2 --> found it! -> return [0,1]
    
        nums = [3, 2, 4], target = 6

        i = 0, num = 3, comp -> 6 - 3 = 3 -> {3:0}
        i = 1, num = 2, comp -> 6 - 2 = 4 -> {3:0, 2:1}
        i = 2, num = 4, comp -> 6 - 4 = 2 -> fount it! -> [1, 2]
        '''

        # visited = {}

        # for i, num in enumerate(nums):
        #     comp = target - num

        #     if comp in visited:
        #         return [visited[comp], i]

        #     visited[num] = i
        
        # return []
