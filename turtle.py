# # try this either as a .py file or in the python shell
# import turtle
# # the distance we want the pointer to travel each time
# DIST = 100
# for x in range(0,6):
#     print "x", x
#     for y in range(1,5):
#         print "y", y
#         # turn the pointer 90 degrees to the right
#         turtle.left(90)
#         # advance according to set distance
#         turtle.forward(DIST)
#     # add to set distance
#     DIST += 20

# import requests
#
# r = requests.get('https://api.github.com/events')
#
# r = requests.post('http://httpbin.org/post', data = {'key':'value'})
#
#
#
# print r['id']

# import md5 # imports the md5 module to generate a hash
# password = 'password';
# # encrypt the password we provided as 32 character string
# encrypted_password = md5.new(password).hexdigest();
# print encrypted_password; #this will show you the encrypted value
# # 5f4dcc3b5aa765d61d8327deb882cf99 -> nice!

# class user(object):
#
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#         self.logged = False
#
#     def login(self):
#         self.login = True
#         print self.name, "is logged in"
#         return self
#
# new_user = user("Anna", "Anna@anna.com")
# print new_user.email
#
# # declare a class and give it name User
# class User(object):
#     # the __init__ method is called every time a new object is created
#     def __init__(self, name, email):
#         # set some instance variables. just like any variable we can call these anything
#         self.name = name
#         self.email = email
#         self.logged = False
#     # this is a method we created to help a user login
#     def login(self):
#         self.logged = True
#         print self.name + " is logged in."
#         return self
# #now create an instance of the class
# new_user = User("Anna","anna@anna.com")
# print new_user.email

class User(object):
    name = "Anna"
anna = User()
print "anna's name: ", anna.name
User.name = "Bob"
print "anna's name after change:", anna.name
bob = User()
print "bob's name:", bob.name
