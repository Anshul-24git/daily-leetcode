class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!= len(t):
                return False
        
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False

        return True

        '''
        "anagram"
        char_count = {}
        1. Processing "s"
        'a' => {'a' : 1}
        'n' => {'a' : 1, 'n' : 1}
        'a' => {'a' : 2, 'n' : 1}
        ..
        ..
        ..
            => {'a' : 3, 'n' : 1, 'g' : 1, 'r' : 1, 'm' : 1}

        2. Process 't' => "nagaram"
        '''

'''
Input - 2 strings s & t
Output - true (if anagram) or false (else)

s = "anagram", t = "nagaram"


'''
        
        
        # seen = set()
        # seen1 = set()

        # if len(s) != len(t):            
        #     return False
            
        # for letter in s:
        #     seen.add(letter)
        # print(seen)


        # for letter1 in t:
        #     seen1.add(letter1)
        #     # print(seen1)

        # if seen == seen1:
        #     # print(seen)
        #     # print(seen1)
        #     return True
        # else:
        #     return False
