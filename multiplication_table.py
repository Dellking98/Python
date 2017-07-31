# Create a program that prints a multiplication table in your console.

print 'x 1 2 3 4 5 6 7 8 9 10 12'

for r in range (1 , 12 + 1):
    display = ""
    for x in range(0, 12 +1):

        if x is 0:
         display += ' ' + str(r)
        else:
            display += ' ' + str(x * r)
    print display
