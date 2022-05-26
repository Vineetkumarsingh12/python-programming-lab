def can_vote(x):
    return x>=18
ages=[34,43,10,17]    # filter accept only ture value.
x=list(filter(can_vote,ages))
print(x)
