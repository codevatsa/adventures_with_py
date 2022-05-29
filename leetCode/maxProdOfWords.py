"""
https://leetcode.com/problems/maximum-product-of-word-lengths/
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
"""

class Solution:
    def maxProduct(self, words):
        wordLen=len(words)
        hashSet = []
        word1 = ""
        word2 = ""
        for i in range(wordLen):
            hashSet.append(set(words[i]))
        max_len_val = 0

        for i in range(wordLen):
            for j in range(i+1, wordLen):
                # set Intersection returns empty set for no intersection i.e unique elements between hash sets
                if not (hashSet[i] & hashSet[j]) and (len(words[i]) * len(words[j])) > max_len_val:
                    word1, word2 = words[i], words[j] 
                    max_len_val= len(words[i]) * len(words[j])
        return max_len_val, word1, word2

words = ["xzqvn","abcw","baz","foo","bar","xtfn","abcdef"]
strModified = Solution()
result = strModified.maxProduct(words=words)
print("Max length: {0} \nWords: {1}, {2}".format(result[0],result[1],result[2]))