class Solution(object):
    def isPalindrome(self, x):
        if x < 0 : 
            return False
        if x == 0 :
            return True
        
        ori = x
        rev = 0
        while x > 0:
            x_last = x % 10
            rev = rev * 10 + x_last
            x //= 10
        if ori == rev:
            return True
        else:
            return False