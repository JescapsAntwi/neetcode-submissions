class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
car fleet -> same position and speed (set of cars)

sort the cars by distances
then find the time it takes for each car to get to the destination/ target 
(target - car_distance) / speed 

right to left operation/ traversal 
when a car collides with another car, its speed slows down to the speed of the car it collided with. so 
we keep the speed of that car ahead

STACK 
the cars are added onto the stack in reverse order (traversing the array in reverse)
then the second car is added onto the stack. their times are calculated and compared.
if they collide, the car on top of the stack is removed/ popped.
we continue this operation until all cars have been traversed and we return the length of our stack
as the number of car fleets 

stack = [3] -> 3
pair = [[1,3], [4, 2]] 
[[4, 2], [1, 2], [0, 1], [7, 1]]


stack = [3, 4.5, 10] -> 3
pair = [[0, 1], [1, 2], [4, 2], [7, 1]]

pop = 1 (3)
        '''
        #pair of cars
        pair = [[p, s] for p, s in zip(position, speed)]
        #stack 
        stack = []
        #iterate in sorted reverse order 
        for p, s in sorted(pair)[::-1]:
              #add times to stack
              stack.append((target - p) / s)
              if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
             #stack length should be more than two for us to pop and check times 
            #pop 
        #return length of stack




      
    