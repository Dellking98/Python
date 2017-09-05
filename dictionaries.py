# # Create a dictionary containing some information about yourself.
# # The keys should include name, age, country of birth, favorite language.
#
# thisIsME = {
# 'name':'Dell',
# 'age':"26",
# 'country of birth':"USA",
# 'favorite':'Red'
# }
#
# def myLife():
#     for key,values in thisIsME.items():
#         print "My", key,  "is" , values
#
#
# myLife()
#
# #prat 1
#
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# for val in students:
#     # length = 0
#     # length = len(students)
#     print val["first_name"],val['last_name']
#
#
# # part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# print users['Students'][0]['first_name'],users['Students'][0]['last_name']


def user1():
    import random
    num = 0

    for val in users.keys():
        x = users[val]
        print val
        for i in x:
            num +=1
            length = len(i['first_name']) + len(i['last_name'])
            print num, "-",  i['first_name'], i['last_name'],"-" , length

# print len(users['Instructors'][0]['first_name'])
user1()
