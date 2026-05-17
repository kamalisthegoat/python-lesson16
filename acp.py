try:
    print("welcome to the party ur age must be above 14")

    age = int(input("enter your age: "))
    if (age < 14):
        raise ValueError
    else:
        print("your age is above 14 your allowed to go in, your age is", age)

except ValueError:
    print("your below the age of 14,and not allowed to go inside .Your age is", age )

if age % 2 == 0:
    print("your age is a even number")

else:
    print("your age is a odd number")            