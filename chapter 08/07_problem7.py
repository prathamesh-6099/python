# Write a python function to remove a given word from a list ad strip it at the same 
# time.
def rem(l,word):
    n=[]
    for iteem in l:
        if(iteem!=word):
            n.append(iteem.strip(word))
    return n

l=["Harray", "Rohan", "Shubham", "an"]
print(rem(l,"a"))