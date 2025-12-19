class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups = {}

        # for word in strs:
        #     count = [0] * 26
        #     for ch in word:
        #         index = ord(ch) - ord('a')
        #         count[index] += 1

        #     key = tuple(count)

        #     if key not in groups:
        #         groups[key] = []
        #     groups[key].append(word)

        # return list(groups.values())


        anagram_map = {}

        #Input: strs = ["eat","tea","tan","ate","nat","bat"]

        for s in strs:
            key = ''.join(sorted(s))

            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(s)

        return list(anagram_map.values())


        #     sorted_s = ''.join(sorted(s))

        #     if sorted_s in anagram_map:
        #         anagram_map[sorted_s].append(s)
        #     else:
        #         anagram_map[sorted_s] = [s]

        # return list(anagram_map.values())




'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

amagram_map = {}

Process "eat": sorted_form = "aet" = amagram_map = {"aet":["eat"]}
Process "tea": sorted_form = "aet" = amagram_map = {"aet":["eat", "tea"]}
Process "tan": sorted_form = "ant" = amagram_map = {"aet":["eat", "tea"], "ant":["tan"]}
Process "ate": sorted_form = "aet" = amagram_map = {"aet":["eat", "tea", "ate"], "ant":["tan"]}
Process "nat": sorted_form = "ant" = amagram_map = {"aet":["eat", "tea", "ate"], "ant":["tan", "nat"]}
Process "bat": sorted_form = "abt" = amagram_map = {"aet":["eat", "tea", "ate"], "ant":["tan", "nat"], "abt":["bat"]}
return values : [["bat"],["nat","tan"],["ate","eat","tea"]]
sr = sorted(result, key = len)
'''
