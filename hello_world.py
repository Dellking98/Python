# words = "It's thanksgiving day. It's my birthday,too!"
#
# print words.find("day")
#
# words2 = words.replace("day", " month")
#
# print words2
#
# x = [2,54,-2,7,12,100]
#
# print min(x) , max(x)
#
# y = ["hello",2,54,-2,7,12,98,"world"]
#
# print y[0], y[7]
#
# y2 = y[0] , y[7]
#
# print y2
#
# w = [19,2,54,-2,7,12,98,32,10,-3,6]
#
# w.sort()
# print w
#
# w2 = w[:len(w)/2]
# print w2
#
# w3=w[len(w)/2:]
# print w3
#
# w2.insert(0,w3);
#
# print w2

# info = {
# 'name': "Dell",
# 'age': '27',
# 'town': 'Philly',
# 'husband': 'Mike'
# }
#
# def grouping(arr):
#     result = []
#     for key,value in arr.iteritems():
#         # print key
#         # print value
#         result.append((key,value))
#     print result
#
# grouping(info)

# a = "this is a string"
# inhere = ""
#
# for i in a.split():
#     inhere += i[0]
#
# print inhere
#
#
#
# input = "Self contained underwater breathing apparatus"
# output = ""
# for i in input.upper().split():
#     output += i[0]
#
# print output
# a = a.split(" ")
# print a
#
# a = ' '.join(a)
# print a

# def split_and_join(line):
#     w = ''
#     w1 = line.split(" ")
#     print w1
#     w1 = "-".join(w1)
#     print w1
#
# split_and_join("This is great")

# a = "-".join(a)

# def split_and_join(line):
#     line = line.split(" ")
#     line = ('-').join(line)
#     print line
# split_and_join('this is a string')

name = input('What\'s your name? ')

age = int(input('What\'s your age'))

year = (2017 - age)+100

print 'You\'ll be 100 years in' , year

num = int(input('Please give me a number'))

print  num * year


# def gettingNum(num)
    #num = 50  #int(input('Please give me a number'))
    # print num * year

# gettingNum(10)
