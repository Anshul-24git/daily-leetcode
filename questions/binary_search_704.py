class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return -1

'''
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

left = 0, right = 5
1st iteration:
mid = 0 + (5 - 0)//2 = 2
middle num[2] --> 3
3 < 9 --> right half
left = mid + 1 == 3

2nd iteration:
mid = 3 + (5 - 3)// 2 = 4
middle num[4] = 9
9 == 9 --> we found it!!!
return 4
'''
