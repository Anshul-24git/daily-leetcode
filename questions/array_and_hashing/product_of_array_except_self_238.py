class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        #pass 1 (product of left)
        # result[0] = 1
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]

        #pass 2 (product of right and multiply)
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
        """
        i/p : nums = [1,2,3,4]
        o/p : answer = [24,12,8,6]

        Brute force approach:
            0th - 0th*1*2*3
        
        Optimal way:
            prod leftt * prod right
            nums = [1,2,3,4]
            First pass:
                i = 0, result[0] = 1 (no buddy on the left)
                i = 1, res[1] = 1
                .., res[2] = 1*2 = 2
                .., res[3] = 1*2*3 = 6
                => result = [1,1,2,6]
            Second pass:
                res[3] = 1 (lonely on the right) => result = [1,1,2,6]
                res[2] = 4 * 1 => result = [1,1,8,6]
                res[1] = 3 * 4 * 1 => result = [1,12,8,6]
                res[0] = 2 * 3 * 4 => result = [24,12,8,6]
            
        Time : O(n) : 2 passes through the array
        Space : O(1)
        """
        # n = len(nums)
        # result = [0] * n

        # #pass 1 (product of left)
        # result[0] = 1
        # for i in range(1, n):
        #     result[i] = result[i-1] * nums[i-1]

        # #pass 2 (product of right and multiply)
        # right_product = 1
        # for i in range(n-1, -1, -1):
        #     result[i] = result[i] * right_product
        #     right_product *= nums[i]

        # return result

# def test_productExceptSelf():
#     # Test case 1: Basic example
#     assert productExceptSelf([1,2,3,4]) == [24,12,8,6]

# # Run tests
# test_productExceptSelf()
'''        
Input -
    nums[]
Output -
    [] product 1 except self

nums = [1, 2, 3, 4]
return = [24, 12, 8, 6]

answer[i] = left_product[i] * right_product[i]

nums = [1, 2, 3, 4]

left_product: [1, 1, 2, 6]
0th index-
    no left element -> 1
1st index-
    left of 2 -> 1
2nd index-
    left of 3 -> 1*2 = 2
3rd index-
    left of 4 -> 1 * 2 * 3 = 6

right_product : [24, 12, 4, 1]



        n = len(nums)
        answer = [1] * n

        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i] 

        return answer
'''
