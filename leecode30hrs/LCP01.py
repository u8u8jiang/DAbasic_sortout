
# LCP01
import numpy as np

class Solution(object):
    def game(self, guess, answer):
       
        count = 0
        for i in range(3):
            if guess[i] == answer[i]:
                count = count + 1
        return count


