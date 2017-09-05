#
# l = ['magical unicorns',19,'hello',98.89,'world']
# lA = [2,3,1,7,4,12]
# sA = ["car", 'DoJO', 'sleeping']
#
# sum = 0;
# new_string = ""
#
# testing = lA
# new_arr = ""
#
# for i in range(0,len(testing)):
#
#     if isinstance(testing, int) == int:
#         new_arr = "int"
#
#     elif isinstance(testing, str) == str:
#         new_arr = "str"
#
#     else:
#         new_arr = 'mixed'
#
# for x in range(0,len(tesing)):
#
#     if type(l) is int:
#         sum1 = sum + testing[x]
#
#     elif type(l) is str:
#         new_string.append(x)
#
# if new_arr == "int":
#     print "Sum:", sum1
# elif new_arr == "str":
#     print "String :", new_string
# elif new_arr == 'mixed':
#     print "This is a Mixed List"
#     print "String :", new_string
#     print "Sum:", sum1

# l = [1,2,34,5]
#
#
# print sum(l)





# a = [2,5,8,-65,0,-3,45]
# b = ["horses","chickens","rabbits"]
# ab = ["horses",5,-17,"cows",67.43,"birds",-3.4]
# l = ['magical unicorns',19,'hello',98.98,'world']
# sum = 0
# new_string = ""
#
# example = l
# array = ""
#
# for i in range(0,len(example)):
#     if all(isinstance(example,int) for example in example):
#         array = "int"
#     elif all(isinstance(example,str) for example in example):
#         array = "str"
#     else:
#         array = "mixed"
#
# for idx in range(0,len(example)):
#     if type(example[idx]) is int:
#         sum = sum + example[idx]
#     elif type(example[idx]) is str:
#         new_string = new_string +" " + example[idx]
#
#
# if array == "int":
#     print "The array you entered is of integer type"
#     print "Sum:",sum
# elif array == "str":
#     print "The array you entered is of string type"
#     print "String:",new_string
# elif array == "mixed":
#     print "The array you entered is of mixed type"
#     print "String:",new_string
#     print "Sum:",sum

# gallon = 128
#
# def orange(cup):
#     cup1 = gallon/cup
#
#     print cup1
#
#
# orange(8)


def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    print arr
    return arr

multiply ([2,4,10,16], 5)

# a = [2,4,10,16]
# b = multiply(a,5)i
# print b

# # output:
# >>>[2,4,10,16]
