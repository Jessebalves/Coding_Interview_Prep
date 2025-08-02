#You are given a string s. 
#The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
#Return the score of s.

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0 
        
        #you can find the ascii value of a character using ord()
        #abs is a built in function
        for i in range(0,len(s) - 1):
            sum +=  abs(ord(s[i]) - ord(s[i+1]))
        return sum
