class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        max_length = 0

        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length
        # if not s:
        #     return 0
        
        # char_index ={}

        # start = 0
        # max_length = 0

        # for end in range(len(s)):
        #     if s[end] in char_index and char_index[s[end]] >= start:
        #         start = char_index[s[end]] + 1
        #     else:
        #         max_length = max(max_length, end - start + 1)

        #     char_index[s[end]] = end

        # return max_length

        '''
        2 pointers - sliding window
            L, R pointers while maintaining sliding window
            Expand window - move right pointer initially
            set to track current items
            if dup found:
                move left pointer
            keep updating the length

        Input: s = "abcabcbb"
        Output: 3

        window "a" -> length = 1 | right ++
        window "ab" -> length = 2 | right ++
        window "abc" -> lenght = 3 | right ++
            moving ahead, found dup 'a'
        window ""
        '''
