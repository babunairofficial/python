# Sets

set1 = {"Roger", "Syd"}
set2 = {"Roger"}

intersect = set1 & set2
print(intersect)

mod = set1 | set2 #union of two sets
print(mod)

diff = set1 - set2 #difference between two sets
print(diff)

subs = set1 > set2 #set1 subset of set2 - true
print(subs)

subs2 = set1 < set2 #set2 subset of set1 - false
print(subs2)

print(list(set1)) #print elements of set as list