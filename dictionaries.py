# Create a dictionary containing some information about yourself.
# The keys should include name, age, country of birth, favorite language.

thisIsME = {
'name':'Dell',
'age':"26",
'country of birth':"USA",
'favorite':'Red'
}

def myLife():
    for key,values in thisIsME.items():
        print "My", key,  "is" , values


myLife()
