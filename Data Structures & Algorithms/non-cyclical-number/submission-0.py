class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set() #hashset 

        while n not in visit:
            visit.add(n)
            n = self.squareDigits(n)
            if n == 1:
                return True 
        return False 
        #if n <= 0:
        #return False 
    

    def squareDigits(self, n:int) -> int:
        output = 0

        while n:
            digit = n % 10 #isolate last digit 
            digit = digit ** 2 # square digit 
            output += digit 
            n = n // 10 # digits before last digits 
        return output 



# {110} 
#output = 0,1, 

# digit = 0, 0
# output = 2
#  n = 0