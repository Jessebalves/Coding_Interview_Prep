class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = ['a','e','i','o','u']
        vowel_count = 0
        cons_count = 0 

        for value in s:
            if value in vowels:
                if vowel_count < s.count(value):
                    vowel_count = s.count(value)
            else:
                if cons_count < s.count(value):
                    cons_count = s.count(value)
        print(vowel_count)
        print(cons_count)
        return vowel_count + cons_count
