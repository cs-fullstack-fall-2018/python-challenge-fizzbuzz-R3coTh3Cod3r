

# Iterate from 0 to 100
# number is evenly divisible by 5, write 
# number of fives.txt else print number on screen.

#
# my_file = open("fives.txt", "w+")
#
# for num in range(0, 101):
#     if num % 5 == 0:
#         my_file.write(str(num) + "/n")
#     else:
#         print("Not divisible by 5: ", num)

import os

os.system("clear")
my_file = open("FizzBuzz.txt", "w+")
for num in range(1,100):
    if num % 3 == 0 and num % 5== 0:
        print(str(num),"FIZZBUZZ")
        my_file.write("FizzBuzz.txt")
    elif num % 5 == 0:
        print(str(num),"BUZZ")
    elif num% 3 == 0:
        print(str(num),"FIZZ")
    else:
        print(num)



