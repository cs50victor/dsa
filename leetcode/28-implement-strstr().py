"""
Tags: Arrays

Notes: A mix of math and understanding of how the range function works.
	- for i in range(0, len(haystack), lenOfNeedle)  wouldn't work because the needle substring might not start at the current index but it could start anywhere within the range(i,lenOfNeedle)
	- the last possible index to find the needle is at len(haystack)-lenOfNeedle
	- so we use range(len(haystack)-lenOfNeedle+1)
	- 
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        lenofNeedle = len(needle)
        
        for i in range(len(haystack)-lenofNeedle+1):
            if haystack[i] == needle[0]:
                # start looking
                if haystack[i:i+lenofNeedle] == needle:
                    return i
        return -1