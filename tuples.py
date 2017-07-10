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

def tuples(arr):

    key = arr.iterkeys()
    values = arr.itervalues()
    print zip(key, values)


tuples(my_dict)


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def makingDict(arr1 , arr2):
    new_dict = zip(arr1, arr2)
    new_dict2 = dict(new_dict)
    print new_dict2

makingDict(name,favorite_animal)

