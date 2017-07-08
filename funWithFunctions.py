# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
#
# Your program output should look like below:

# def odd_even():
#     for i in range(1,2000+1):
#         if i % 2 != 0:
#             print "Number is" , i , "This is an odd numder"
#         else:
#             print "Number is" , i , "This is an Even numder"
#
# odd_even()

# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
#
# The function should multiply each value in the list by the second argument. For example, let's say:

def multiply(v_list, numder):
    for i in range(len(v_list)):
        v_list[i] *= numder
    return v_list

print multiply([2,4,5,6,2], 5)

# Write a function that takes the multiply function call as an argument.
# Your new function should return the multiplied list as a two-dimensional list. Each internal list should
# contain the number of 1's as the number in the original list. Here's an example:
    # needed help
def multiply_arr(arr):
    print arr
    new_arr = []
    for i in arr:
        val_arr = []
        for x in range (0,i):
            val_arr.append(1)
        new_arr.append(val_arr)
    return new_arr

a = multiply_arr(multiply([3,2,3,4,],1))
print a



# def multiply_arr(arr):
#     print arr
#     new_arr =[]
#     for a in arr:
#         val_arr = []
#         for w in range(0,a):
#             val_arr.append(1)
#         new_arr.append(val_arr)
#     return new_arr
#
# a = multiply_arr(multiply([3,3,1,2,3],3))
# print a
