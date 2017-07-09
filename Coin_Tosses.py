
def coing_tosses(Tosses):
    head = 0
    tails = 0
    for attempt in range(1,Tosses):
        import random
        random_number = random.random()
        if random_number < 0.5:
            head += 1
            print "Attemp #" ,str(attempt)+": Throwing a coin.. It's a head!...Got" , str(head), "head(s) so far and",str(tails),"tails(s) so far"
        else:
            tails += 1
            print "Attemp #" ,str(attempt)+": Throwing a coin.. It's a tails!...Got" , str(head), "head(s) so far and",str(tails),"tails(s) so far"


coing_tosses(5001)
