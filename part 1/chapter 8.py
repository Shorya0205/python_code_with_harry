#Sets 
e={}#it is an empty dictionary
#For empty set
s=set()
#in set no repetion is allowed
#order is not preserved

#set methods
#1.
s.add(1)  # Adding an element to the set
s.add(2)  # Adding another element to the set
s.add(3)  # Adding a third element to the set
s.add(1)  # Adding an existing element (no effect, as sets do not allow duplicates)
print(s)  # Output: {1, 2, 3}
#2. remove()
s.remove(2)  # Removing an element from the set
print(s)  # Output: {1, 3}
#3. discard()
s.discard(3)  # Discarding an element (no error if it doesn't exist)
print(s)  # Output: {1}
#4. pop()
s.pop()  # Removing and returning an arbitrary element from the set ,RANDOM
print(s)  # Output: set is now empty        
#5. clear()
s.clear()  # Removing all elements from the set 
print(s)  # Output: set is now empty
#6. union()
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)  # Union of two sets
print(s3)  # Output: {1, 2, 3, 4, 5}
#7. intersection()
s4 = s1.intersection(s2)  # Intersection of two sets
print(s4)  # Output: {3}
#8. difference()
s5 = s1.difference(s2)  # Difference of two sets
print(s5)  # Output: {1, 2}
#9.subset()
s6 = {1, 2}
s7 = {1, 2, 3}
print(s6.issubset(s7))  # Checking if s6 is a subset of s7, Output: True
#10.superset()
print(s7.issuperset(s6))  # Checking if s7 is a superset of s6, Output: True