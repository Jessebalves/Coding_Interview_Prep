# There is a programming language with only four operations and one variable X:

# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.


class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        number = 0 
        for i in range(len(operations)):
            if operations[i] in ["--X","X--"]:
                number -= 1
            elif operations[i] in ["++X","X++"]:
                number += 1
        return number
