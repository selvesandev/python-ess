s = {1, 2}
s.add(3)
print(s)

# s.clear()
print(s)

sc = s.copy()  # Creating a new copy
# Changing the value of copy won't effect the original


sc.add(2)
print(sc)

diff = {1, 2, 3, 4, 5}.difference({1, 2, 3, 4})
print(diff)  # 5

s = {1, 2, 3}
s.difference_update({1, 4, 5})
print(s)

s = {1, 2, 3, 4}
s.discard(2)
print(s)  # {1,3,4}  remove the element if it's a member

s1 = {1, 2, 3}
s2 = {1, 2, 4}
# print(s1.intersection(s2))  # {1,2}  # common to both of the set


s1.intersection_update(s2)
print(s1)  # updates s1 value with new set i.e the common between both

print({1, 2}.isdisjoint({3, 4}))  # Returns true only if the set values does not match

# Returns the symmetric difference of two sets i.e the value which is on one of the set opposite of intersection
print({1, 2}.symmetric_difference({2, 4}))  # {1, 4}

s1 = {1, 2, 3}
s2 = {1, 2, 4}

s1.update(s2)
print(s1)  # {1,2,3,4}

