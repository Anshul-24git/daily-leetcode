class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            elif current_sum < target:
                left += 1

            else:
                right -= 1

        return []


        '''
        Two pointers as array is already sorted
            left at start | right at the end of array
        if sum < target:
            move the left pointer
        if sum > target:
            move the right pointer
        if sum == target:
            voila, solution found!

        numbers = [2,7,11,15], target = 9
        o/p : [1,2]

        left = 0, right = 3: sum = 2 + 15 -> sum > target => right -- (2)
        left = 0, right = 2: sum = 2 + 11 -> sum > target => right -- (1)
        left = 0, right = 1: sum = 2 + 9 -> sum == target => return value [1,2]
        '''


        # OG 2 sum solution,, just added + 1 in the return statement. Still works
        # Can't use in this question as we need a solution which uses constant space
        # visited = {}

        # for i, num in enumerate(numbers):
        #     comp = target - num

        #     if comp in visited:
        #         return [(visited[comp] + 1), i + 1]

        #     visited[num] = i

        # return False
