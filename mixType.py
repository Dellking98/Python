
l = ['magical unicorns',19,'hello',98.89,'world']
string = []
sum1 = []

for types in l:
    testing = type(types)


    if testing is int:
        sum1.append(types)
        num1 = sum(sum1)

    elif testing is str:
        string.append(types)



print testing
print " String: {}".format(string)
print "Sum:",num1
