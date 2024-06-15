################### Scope ####################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2                # create a new variable or indeedd a new function inside another function- it's only accessible inside that function 
    print(potion_strength)             # Because it has local scope. Its only valid within the walls of this drink_potion()   

drink_potion()
print(potion_strength)

# The only difference between global scope and local socpe ie where you define or create your variable or your functions.
# Global Scope
player_health = 10

def game():                  # The most importent thing to remember from this is if you create a variable within a function, than it's only available within that function.
    def drink_potion():      # But if you create a variable within an if block or a while loop or a for loop or anything that has the indentation and the colon,
        potion_strength = 2  # then that does not count as creating a separate local scope.
        print(player_health) # Why 28 number line is not printed 

    drink_potion()

print(player_health,"Ye wala print ho raha hai")

# There is no Block Scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope
# Usually  a terrible idea to call your local variable and global variable the same name
enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants

# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@yu_angela