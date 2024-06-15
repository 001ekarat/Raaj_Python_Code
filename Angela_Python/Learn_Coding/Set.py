# Set is a data structure which is also called collection of items in which we can represent a group of unique value as a single entity.
# Syntex -- Set_name ={item1, item2, item3, item4, .......itemN} 
# Note :-   * Wrte the Items of set inside the curly brace "{}"
#           * Insertion order is not preserved.
#           * Indexing and slicing not work.
#           * Hetrogenous elemets are allowed.
#           * Mutable in Nature.

var = {}
print(type(var))    # Empty dictionary

var = set()
print(type(var))    #Empty Set


var = {10,'nilesh',47.5,True,'nilesh'}
#print(var[0])       # With the help of indexing we can't acceses particular value , TypeError: 'set' object is not subscriptable
print(type(var))    # Set
print(var)

# var.add('pandey','raaj') , TypeError: set.add() takes exactly one argument (2 given)
#var.update('Learn coding')
print(var)
var.update(["Learn coding" ]) 
#print(var.pop())
#var.remove("nilesh")
var.clear() # Clear all the values from  the set
print(var)

var = {10,'nilesh', True, 'pandey', 56.5, 56, 'raaj'}
var2 = {10,'nilesh', True, 'pandey', 56.5, 56, 'ankit', 'srihan'} # print unique value only

print(var.union(var2))
print(var | var2)

print(var.intersection(var2)) # print common values only
print(var & var2)

print(var.difference(var2))
print(var2 - var)

print(var.symmetric_difference(var2))