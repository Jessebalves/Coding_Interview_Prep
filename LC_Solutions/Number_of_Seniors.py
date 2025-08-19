class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        seniors = 0 

        for value in details:
            print(value[11:13])
            current_num = int(value[11:13])
            if current_num > 60: 
                seniors += 1
        return seniors
