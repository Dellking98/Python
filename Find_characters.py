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





#results = word_list.split(',')
