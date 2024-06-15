
# Dictionaries & Nesting
Dic = {"Ram":"Sita", "Mango" : "Fruit", 123 : 9165}
print(Dic.get("Raam", "Not available"))
print(Dic.keys()) # Show all the Keys
print(Dic.values()) # Show all the values
print(Dic.items())
print(Dic.clear())
Dic = {"Ram":"Sita", "Mango" : "Fruit", 123 : 9165}


for Key, Values in Dic.items():
    print(Key,Values,sep= " - ")





# Dic["Bug"] = ""
# for i in Dic:
#     print(i)
#     print(Dic[i])

# for key in Dic:
#     print(key)
#     print(Dic[key])
# print(Dic)
# print(Dic["Ram"])
# print(Dic.get("123"))
# print(type(Dic))

#1. Dictionary clear() Method
#The clear() method in Python
#
#
#
#
# n is a built-in method that is used to remove all the elements (key-value pairs) from a dictionary.
# It essentially empties the dictionary, leaving it with no key-value pairs
# my_dict = {'1': 'Geeks', '2': 'For', '3': 'Geeks'}
# print(my_dict.get(1))
# my_dict.clear()
# print(my_dict)

# d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
# print(list(d.items())[1][0])
# print(list(d.items())[1][1])