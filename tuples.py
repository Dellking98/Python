my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

# for key in my_dict:
#     x = my_dict[key]
#     print x

# myinfo = zip( my_dict , x)
# print myinfo

<<<<<<< HEAD
def tuples(input_dict):
    result = []
    for key,value in input_dict.items():
        print key, value
        result.append((key, value))
    print result
    return result
    # key = arr.iterkeys()
    # values = arr.itervalues()
    # print zip(key, values)
=======
def tuples(arr):

    key = arr.iterkeys()
    values = arr.itervalues()
    print zip(key, values)
>>>>>>> 9878711c4b76d121acbc1a646c75e85c4c11a2d2


tuples(my_dict)

<<<<<<< HEAD
# Making Dictionaries
# Create a function that takes in two lists and creates a single dictionary where the first list contains keys
# and the second values. Assume the lists will be of equal length.
# Your first function will take in two lists containing some strings. Here are two example lists:
#
# name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
# favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
#
#
# def makingDict(arr1 , arr2):
#     new_dict = zip(arr1, arr2)
#     new_dict2 = dict(new_dict)
#     print new_dict2
#
# makingDict(name,favorite_animal)
=======

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def makingDict(arr1 , arr2):
    new_dict = zip(arr1, arr2)
    new_dict2 = dict(new_dict)
    print new_dict2

makingDict(name,favorite_animal)

>>>>>>> 9878711c4b76d121acbc1a646c75e85c4c11a2d2
