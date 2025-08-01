#Given an input string s, reverse the order of the words.

#A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

#Return a string of the words in reverse order concatenated by a single space.

#Note that s may contain leading or trailing spaces or multiple spaces between two words. 
#The returned string should only have a single space separating the words. Do not include any extra spaces.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_string = ""
        new_words = s.split()
        reversed_words = new_words[::-1]
        print(reversed_words)

        for i in range(len(reversed_words)):
            if i+1 != len(reversed_words):
                new_string += reversed_words[i] + " "
            else:
                new_string += reversed_words[i]

        return new_string
