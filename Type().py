# num = 102
# print (type(num))
# if num >= 100:
#     print "That's a big number!"
# else:
#     print "That's a small number"
# string = 'Exquisite adsdd adwrg hhthii ssdee dsegve adncuhwuhfuiw sbaudhue jnasid'
# print (type(string))
# print len(string)
# if len(string) >= 50:
#      print  "Long sentence."
# else:
#     print  "Short sentence."
# mL = [3,5,7,34,3,2,113,65,8,89]
# print (type(mL))
# if len(mL) >= 10:
#     print "Big list!"
# else:
#     print  "Short list."

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

testing_list = aL

testing_type = type(testing_list)
print testing_type
if testing_type is int:
    if testing_list >= 100:
        print "That's a big number!"
    else:
        print "That's a small number"
elif testing_type is str:
    if len(testing_list) >= 50:
        print "Long sentence."
    else:
        print "Short sentence."
elif testing_type is list:
    if len(testing_list) >= 10:
        print "Big list!"
    else:
        print "Short list."
