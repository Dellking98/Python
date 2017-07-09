# Part I
# Create a function called draw_stars() that takes a list of
# numbers and prints out *.

def draw_stars(arr):
    for x in arr:
        print "*" * x

draw_stars([1,9,3,4])

# Part II
# Modify the function above. Allow a list containing integers and strings
# to be passed to the draw_stars() function. When a string is passed,
# instead of displaying *, display the first letter of the string
# according to the example below. You may use the .lower() string
# method for this part.

def draw_stars2(arr):

    for i in arr:
        if isinstance(i, int):
            print "*" * i
        elif isinstance(i, str):
            w = len(i)
            letter = i[0].lower()
            print letter * w

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x)
