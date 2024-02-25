print("welcome to the automatic pizza order machine!!")
size = input("what size of pizza do you want? L, M, S\n")
pepperoni = input("Do you want pepperoni in it? y or n.\n")
cheese = input("Do you want extra cheese? y or n.\n")
price = 0

if size == "L":
    price = 25
    if pepperoni == "y":
        price += 3
    if cheese == "y":
        price += 1
    print(f"Your final bill is: {price}$")
elif size == "M":
    price = 20
    if pepperoni == "y":
        price += 3
    if cheese == "y":
        price += 1
    print(f'Your final bill is: {price}$')
elif size == "S":
    price += 15
    if pepperoni == "y":
        price += 2
    if cheese == "y":
        price += 1
    print(f"Your final bill is: {price}$")
