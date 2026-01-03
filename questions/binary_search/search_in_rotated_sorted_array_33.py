class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            #target in left half
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
        '''
        Identify the sorted half first
        Check which half target lies and continue serch there
        Otherwise search the other half
        Repeat until found

        Array: [4,5,6,7,0,1,2], Target: 0
        
        Step 1:
        left = 0, right = 6 => mid = 3, num[mid] = 7

        '''
