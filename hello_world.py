words = "It's thanksgiving day. It's my birthday,too!"

print words.find("day")

words2 = words.replace("day", " month")

print words2

x = [2,54,-2,7,12,100]

print min(x) , max(x)

y = ["hello",2,54,-2,7,12,98,"world"]

print y[0], y[7]

y2 = y[0] , y[7]

print y2

w = [19,2,54,-2,7,12,98,32,10,-3,6]

w.sort()
print w

w2 = w[:len(w)/2]
print w2

w3=w[len(w)/2:]
print w3

w2.insert(0,w3);

print w2
