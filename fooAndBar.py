# Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.
# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square.
# If it is a prime number print "Foo". If it is a perfect square print "Bar". If it is neither print "FooBar".
# Do not use the python math library for this exercise. For example, if the number you are evaluating is 25,
# you will have to figure out if it is a perfect square. It is, so print "Bar".


# def fooBar():
#
#     row = ' '

for num in range (100,1001):
    for w in range (2,num):
        if num % w == 0 and num % w != 0 :
            print num, "FooBar"
            break
        elif num % w == 0:
            print num, "Bar"
            break
    if num % w != 0:
        print num, "Foo"
            # break


# for num in range(100,1000):  #to iterate between 10 to 20
#    for i in range(2,num): #to iterate on the factors of the number
#     if num%i == 0:      #to determine the first factor
#         j=num/i          #to calculate the second factor
#         print '%d is a perfect' % (num)
#         break #to move to the next number, the #first FOR
#    else:                  # else part of the loop
#       print num, 'is a prime number'

# for num in range(100,1001):
#     prime = True
#     for i in range(2,num):
#         if (num%i==0):
#             prime = False
#             perfect = num%i==0
#     print perfect, "perfect"
#     if prime:
#        print num, "is a prime number"
