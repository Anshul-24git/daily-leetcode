class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target_count = {}
        for char in t:
            target_count[char] = target_count.get(char, 0) + 1

        left = 0
        right = 0
        required = len(target_count)
        formed = 0

        window_counts = {}

        min_len = float('inf')
        min_left = 0

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in target_count and window_counts[char] == target_count[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                window_counts[char] -= 1
                if char in target_count and window_counts[char] < target_count[char]:
                    formed -= 1

                left += 1

            right += 1

        return "" if min_len == float('inf') else s[min_left:min_left + min_len]
        
        '''
        2 strings:
            s(m) & t(n)
        Two pointer - Sliding Window Approach
            Setup:
                2 pointers (L, R)
                Frequency map
                Start by moving right pointer till we find a valid range
                    once we find this range
                        move the left pointer till we come across invalid range
                While tracking the minimum valid window

        Input: s = "ADOBECODEBANC", t = "ABC"
        Step 1 :
            start with min 3 chars and we'll expand the window till we find all of 't'
            "ADOBEC" -> valid becausecontains : "ABC"
             L     R
        Step 2 :
            "ADOBEC" : contract from left
            Remove A : "DOBEC" 

             BANC
             L  R   

        Output: "BANC"
        '''
