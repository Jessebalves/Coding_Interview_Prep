#Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first
#occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word

        counter = 0 
        for i in range(len(word)):
            if ch == word[i]:
                break
            else:
                counter += 1

        print("Counter",counter)
        reversed_string = word[counter::-1]
        print("huh",reversed_string)
        for i in range(counter+1,len(word)):
            reversed_string += word[i]
        return reversed_string
