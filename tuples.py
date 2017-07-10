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
