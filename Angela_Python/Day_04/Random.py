import random # random is a python module

# random_integer = random.randint(1,15)
# print(random_integer)

# 0.00000 - 0.99999...
random_float = random.random()
print(random_float)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")


random_site = random.randint(0,1)

if random_site == 1:
    print("Head")

else:
    print("tail")