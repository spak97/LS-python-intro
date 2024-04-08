# refactor so you don't need two invocations of randrange
import random

highest = 10
number = 0
print(number)

while number != highest:
    number = random.randrange(highest + 1)
    print(number)