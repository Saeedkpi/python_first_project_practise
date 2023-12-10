height = int(input("What is your height in feet?"))

if height >= 3:
    print("You can ride")
    age = int(input("What is your age?"))
    if age <=18:
        print("Pay 500tk")
    else:
        print("Pay 1000tk")
else:
    print("Can't ride")
print("Bye")

#if-elif-else condition

number = int(input("Enter Number "))

if number == 1:
    print("one")
elif number == 2:
    print("Two")
elif number == 3:
    print("Three")
elif number == 4:
    print("Four")
else:
    print("Wrong Input")
print("Bye")