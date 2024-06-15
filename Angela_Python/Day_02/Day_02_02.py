print("welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoster!")
    age = int(input("what is your age"))
    if age <= 12:
        bill = 7
        print("Child tickets are 7$.")
    elif age <= 18:
        bill = 15
        print("Youth tickets are 15$")

    else:
        bill = 18
        print("Adult tickets are 18$.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3 # same as bill = bill + 3
    print(f"Your final bill is {bill}")

else:
    print("Sorry , you have to grow taller to ride rollercoaster")