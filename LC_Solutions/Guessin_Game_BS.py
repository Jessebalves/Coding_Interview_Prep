#We are playing the Guess Game. The game is as follows:
#I pick a number from 1 to n. You have to guess which number I picked.
#Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
#You call a pre-defined API int guess(int num), which returns three possible results:
#-1: Your guess is higher than the number I picked (i.e. num > pick).
#1: Your guess is lower than the number I picked (i.e. num < pick).
#0: your guess is equal to the number I picked (i.e. num == pick).
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1 
        right = n 

        while left <= right:
            middle = (left+right) // 2
            result = guess(middle)
            if result == 0 :
                return middle
            elif result == 1:
                left = middle + 1
            else:
                right = middle - 1
