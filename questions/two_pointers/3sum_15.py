class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        if n < 3:
            return []

        for i in range(n - 2):
            #break early as sum can't be negative if 1st element is +ve
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result

        '''
        1. Sort the array
        2. Fix the first number
        3. 2 pointers (left and right) : find pairs which will make the sume -ve

        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        result = []
        1.
            sorted nums = [-4, -1, -1, 0, 1, 2]
        2. 
            i = 0, num[i] = -4 , left[i+1] = -1, right[n-1] = 2
                (-4 + (-1) + 2) < 0, left ++
                (-4 + (-1) + 2) < 0, left ++
                (-4 + (0) + 2) < 0, left ++
                (-4 + (1) + 2) < 0, left ++
            i = 1, num[i] = -1 , left[i+1] = -1, right[n-1] = 2
                (-1 + (-1) + 2) = 0 : Found a pair result = [[-1, -1, 2]]
        '''
