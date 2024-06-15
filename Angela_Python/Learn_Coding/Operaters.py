# Operator is nothing but symbols that perform certain task.

# Various set of operators in python :-
#   Arthematic Operator (+, -, *, /, //, **)
#   Relational Operator or Comparison operator (<, <=, >, >=, ==, !=, )
#   Logical Operator:- and, or, not
#   Bitwise operator (applicable for int and bool value only):- 
#                   & -> bitwise and (if both 1 then 1 else 0)
#                   | -> bitwise or (if any 1 then 1 else 0)
#                   ^ -> if both same then output 0 else 1
#                   ~ -> Bitwise Complement
#                   >> -> Binary shift right
#                   << -> Binary shift left
#   Assingment operator =
#   Special operator:- a) Identity Operator 
#                         is, is not
#                      b)Membership Operator
#                        in, not in 

a = 13
b = 2

print(a<b and a>b) #false
print(a>b or a<b) #True
print(not(a<b and a>b)) #True
print(5 & 6) # bitwise and
print(5 | 6) # bitwise or
