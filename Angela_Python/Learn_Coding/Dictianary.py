# Dictianary is a data structure in which we represent a group of object as KEY-VALUE pair.
# Syntax:- dict_name = {key:value}
# Note:-    * Indexing & Slicing not work.
#           * Insertion order is preserved
#           * Hetrogenous elements are allowed.
#           * Mutable in nature.
#           * Key must be unique , but dublicates value are allowed

var = {}
print(type(var))
var = dict()
print(type(var))

Dic = {"Ram":"Sita", "Mango" : "Fruit", 123 : 9165}
print(Dic.get("Raam", "Not available"))
print(Dic.keys()) # Show all the Keys
print(Dic.values()) # Show all the values
print(Dic.items())
print(Dic.clear())