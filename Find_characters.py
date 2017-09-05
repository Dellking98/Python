<<<<<<< HEAD
#
# word_list = ['hello','world','my','name','is','Anna']
# char = 'i'
#
# new_arr = []
#
# for i in word_list:
#     if i.find(char) != -1:
#         new_arr.append(i)
#
# print new_arr

word_list = ["hello","world","my","name","is","Anna"]
char = "m"
new_list = []

for idx in range (0,len(word_list)):
    if word_list[idx].count(char) > 0:
        new_list.append(word_list[idx])

print "new_list =",new_list
=======

word_list = ['hello','world','my','name','is','Anna']
char = 'i'

new_arr = []

for i in word_list:
    if i.find(char) != -1:
        new_arr.append(i)

print new_arr
>>>>>>> 9878711c4b76d121acbc1a646c75e85c4c11a2d2





#results = word_list.split(',')
