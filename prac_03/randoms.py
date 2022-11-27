
import random
print(random.randint(5, 20))  # line 1
"""
What did you see on line 1?
integer number
What was the smallest number you could have seen, what was the largest?
smallest: 5
largest: 20
"""

print(random.randrange(3, 10, 2))  # line 2

"""
What did you see on line 2?
integer number
What was the smallest number you could have seen, what was the largest?
smallest: 3
largest: 9
Could line 2 have produced a 4?
NO
"""

print(random.uniform(2.5, 5.5))  # line 3
"""
What did you see on line 3?
A number between 2.5 and 5.5
What was the smallest number you could have seen, what was the largest?
smallest: 2.5000000000000
largest: 5.5000000000
"""
numbers = random.uniform(1, 100)
print("{:.2f}".format(numbers))

