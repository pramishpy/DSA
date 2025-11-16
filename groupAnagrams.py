from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        #hash map to store grouped anagrams
        res = defaultdict(list)
        for s in strs: #s is each word in the input list
            #array to store character counts in each word
            count = [0] * 26
            for char in s: #char is each character in the word
                count[ord(char) - ord('a')] += 1 #if ord("b") = 98 and ord("a") = 97, then index for "b" is 1
            res[tuple(count)].append(s) #
        return list(res.values())
if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]