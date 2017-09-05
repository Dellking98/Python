
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
#
# import random
#
# def toss(reps):
#     # print new_toss
#     attempt_count = 1
#     head_count = 0
#     tail_count = 0
#     result = ""
#     result_string_complete = ""
#
#     for x in range(1, reps):
#         new_toss = random.randint(0,1)
#         if new_toss == 1:
#             head_count += 1
#             result = "head"
#             print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
#         else:
#             tail_count += 1
#             result = "tail"
#             print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
#         attempt_count += 1
#
# toss(5001)
