class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}

        left = 0

        max_freq = 0

        max_length = 0

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            max_freq = max(max_freq, char_count[s[right]])

            window_size = right - left + 1

            if window_size - max_freq > k:
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
        
        '''
        s = "ABAB", k = 2
        o/p : 4
        s = "AABABBA", k = 1
        o/p : 4

        Approach:
            Use sliding window - with left and right pointers
            Track frequency of each char
            Track max_freq - this will remain constant till we find a greater freq
            if window_size - max_freq > k
                shrink from left
            update max length
        Time : O(n)
        Space : O(1)

        Example walkthrough:

        s = "ABAB", k = 2
        
    Step-by-step execution:
    right=0: s[0]='A', char_count={'A':1}, max_freq=1, window_size=1, changes=0≤2 ✓, max_length=1
    right=1: s[1]='B', char_count={'A':1,'B':1}, max_freq=1, window_size=2, changes=1≤2 ✓, max_length=2  
    right=2: s[2]='A', char_count={'A':2,'B':1}, max_freq=2, window_size=3, changes=1≤2 ✓, max_length=3
    right=3: s[3]='B', char_count={'A':2,'B':2}, max_freq=2, window_size=4, changes=2≤2 ✓, max_length=4

    Output: 4 ✓
        '''
    # # Dictionary to store character frequencies in current window
    #     char_count = {}
    #     # Left pointer of sliding window
    #     left = 0
    #     # Track maximum frequency of any character in current window
    #     max_freq = 0
    #     # Result: maximum length found so far
    #     max_length = 0
        
    #     # Right pointer expands the window
    #     for right in range(len(s)):
    #         # Add current character to window
    #         char_count[s[right]] = char_count.get(s[right], 0) + 1
            
    #         # Update maximum frequency in current window
    #         max_freq = max(max_freq, char_count[s[right]])
            
    #         # Current window size
    #         window_size = right - left + 1
            
    #         # Operations needed = window_size - max_frequency_character
    #         operations_needed = window_size - max_freq
            
    #         # If operations needed exceed k, shrink window from left
    #         if operations_needed > k:
    #             # Remove leftmost character from window
    #             char_count[s[left]] -= 1
    #             # Move left pointer to shrink window
    #             left += 1
            
    #         # Update maximum length (window is valid here)
    #         max_length = max(max_length, right - left + 1)
        
    #     return max_length    
        
        '''
        s = "ABAB", k = 2
        string s
        integer k

        A-Z
        26

        s = "ABAB", k = 2

        'A'
        char_count - {'A':1}

        '''
