class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

        """
        1. 2 pointers approach
            left and right : starting from both the ends
        2. Skip the ineligible/non-alphanumeric chars
        3. Character comparision with both pointers
        4. If we don't find any matching character, we'll exit early

        Input: s = "A man, a plan, a canal: Panama"
            cleaned_input : "amanaplanacanalpanama"
        left = 0 ('A'), len(s) - 1 ('a') -> matches
        left = 2 ('m'), len - 2 -> matches
        continue this till we find a distinct char
            if none found :
                true
            else
                false
        """
        # left, right = 0, len(s) - 1

        # while left < right:
        #     while left < right and not s[left].isalnum():
        #         left += 1

        #     while left < right and not s[right].isalnum():
        #         right -= 1

        #     if s[left].lower() != s[right].lower():
        #         return False

        #     left += 1
        #     right -= 1

        # return True
