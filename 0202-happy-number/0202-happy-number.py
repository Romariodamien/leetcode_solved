class Solution:
    def isHappy(self, n: int) -> bool:
        
        l = []
        while n != 1:
            l.append(n)
            s = 0
            for i in str(n):
                s += int(i) ** 2
            if s in l:
                return False
            n = s
        return True
