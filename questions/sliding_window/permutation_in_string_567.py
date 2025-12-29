class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = {}
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1
        
        window_size = len(s1)
        window_freq = {}

        for i in range(window_size):
            char = s2[i]
            window_freq[char] = window_freq.get(char, 0) + 1

        if window_freq == s1_freq:
            return True

        for i in range(window_size, len(s2)):
            new_char = s2[i]
            window_freq[new_char] = window_freq.get(new_char, 0) + 1

            old_char = s2[i - window_size]
            window_freq[old_char] -= 1

            if window_freq[old_char] == 0:
                del window_freq[old_char]

            if window_freq == s1_freq:
                return True

        return False

        #Solution 2: Canonical 26-array + matches (fastest + best for interview)

    # if len(s1) > len(s2):
    #     return False

    # need = [0] * 26
    # win  = [0] * 26

    # for ch in s1:
    #     need[ord(ch) - ord('a')] += 1

    # k = len(s1)

    # for i in range(k):
    #     win[ord(s2[i]) - ord('a')] += 1

    # matches = 0
    # for i in range(26):
    #     if win[i] == need[i]:
    #         matches += 1

    # if matches == 26:
    #     return True

    # for r in range(k, len(s2)):
    #     add = ord(s2[r]) - ord('a')
    #     rem = ord(s2[r - k]) - ord('a')

    #     # add char
    #     if win[add] == need[add]:
    #         matches -= 1
    #     win[add] += 1
    #     if win[add] == need[add]:
    #         matches += 1

    #     # remove char
    #     if win[rem] == need[rem]:
    #         matches -= 1
    #     win[rem] -= 1
    #     if win[rem] == need[rem]:
    #         matches += 1

    #     if matches == 26:
    #         return True

    # return False

        # Just my try, not a solution
        # left = 0
        # # res = []
        # s1r = s1[::-1]
        # print(s1r)
        # print(s2)
        # for right in range(len(s2)):
        #     if s1 or s1r in s2:
        #         return True
        #     else:
        #         return False
        # return []
