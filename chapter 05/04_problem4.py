# What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?
s = set()
s.add(20)
s.add(20.0)
s.add('20') 
print(len(s))
# its length is 2 bcz, s.add(20.0): Here, 20.0 (a float) is considered the same as 20 (an integer) because they are numerically equivalent. So, the set still contains only {20}.
