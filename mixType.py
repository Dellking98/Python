
l = ['magical unicorns',19,'hello',98.89,'world']
lA = [2,3,1,7,4,12]
sA = ["car", 'DoJO', 'sleeping']

sum = 0;
new_string = ""

testing = lA
new_arr = ""

for i in range(0,len(testing)):

    if isinstance(testing, int) == int:
        new_arr = "int"

    elif isinstance(testing, str) == str:
        new_arr = "str"

    else:
        new_arr = 'mixed'

for x in range(0,len(tesing)):

    if type(l) is int:
        sum1 = sum + testing[x]

    elif type(l) is str:
        new_string.append(x)

if new_arr == "int":
    print "Sum:", sum1
elif new_arr == "str":
    print "String :", new_string
elif new_arr == 'mixed':
    print "This is a Mixed List"
    print "String :", new_string
    print "Sum:", sum1
