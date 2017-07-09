import random

def grading():
    for w in range(0,10):
        opt = random.randint(60,100)
        if opt >= 90 :
            print "Score:" , opt , "Your grade is A"
        elif opt >= 80:
            print "Score:", opt , "Your gade is B"
        elif opt >= 70:
            print "Score:", opt , "Your gade is c"
        else:
            print "Score:", opt , "Your gade is D"



grading()
print "The Program is done. Bye now"
